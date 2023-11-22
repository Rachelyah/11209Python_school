'''
cpbl
'''

import tkinter as tk
from tkinter import ttk
from cpbl_treeview import cpblTreeView
from cpbl_treeview import InfoDisplay
from tkinter import messagebox
from threading import Timer
import datasource
from PIL import Image
import infoFrame


#自定義class 呼叫datasource讀取csv檔案跟匯入資料庫的function
class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except Exception: 
            messagebox.showerror('錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() 

#-------------------------------建立介面--------------------------------------------
#------------------------------最上面的標題---------------------------------------
        topFrame =tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        #只要裡面有內容，topFrame的邊框&預設大小就會失效，除非下Label的邊框距離設定
        #建立Label標籤放在topFrame裡面，設定與邊框的距離
        tk.Label(topFrame,text='中華職棒球員資料查詢',font=('arial,40'),bg='#333333',fg='#FFFFFF',pady=20).pack(fill='both', pady=20, padx=20)  
        topFrame.pack(pady=30)

#-----------------------------建立查詢介面-----------------------------------
        #建立容器元素
        middleFrame = ttk.LabelFrame(self,text='',relief=tk.GROOVE,borderwidth=1)
        
        #建立標籤
        tk.Label(middleFrame,text='球員搜尋').pack(side='left')

        #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.on_key_release)
        search_entry.pack(side='left')     
        middleFrame.pack(fill='x',padx=20)


#------------------------------球員個人資料、PR數據---------------------------------------
        
        info_main_Frame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        info_display = InfoDisplay.create_widgets(info_main_Frame)
        info_main_Frame.pack()


##-----------------------------建立隊伍按鈕-----------------------------------

        middle1Frame = ttk.LabelFrame(self,text='選擇球隊',relief=tk.GROOVE,borderwidth=1)
        tk.Label(middle1Frame,text='選擇球隊').pack
        middle1Frame.pack(fill='x', padx=20, pady=20)

        def team_search(event:None, word:str):
            print(word)
            rows = datasource.search_by_team(event=None, word=word)
            self.cpblTreeView.update_content(site_datas=rows)

        tk.Button(middle1Frame, text='中信兄弟', command=lambda: team_search(event=None,word='中信')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='樂天桃猿',command=lambda: team_search(event=None,word='樂天')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='統一7-ELEVEn獅',command=lambda: team_search(event=None,word='統一')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='富邦悍將',command=lambda: team_search(event=None,word='富邦')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='味全龍',command=lambda: team_search(event=None,word='味全')).pack(ipadx=25, ipady=10, side='left', expand='Yes')

#------------------------------建立treeView-----------------------------------------
        bottomFrame = tk.Frame(self)
        self.cpblTreeView = cpblTreeView(bottomFrame
                                                               ,columns=('Year','Team Name','ID','Name','G', 'GS', 'GR', 'W', 'L', 'SV', 'HLD', 'IP', 'BF', 'H', 'HR', 'BB', 'SO', 'ER')
                                                               ,show="headings"
                                                               ,height=20)
        #設定捲動軸 
        self.cpblTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.cpblTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.cpblTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20) #pady=(與上段距離，與下段距離)
        
#-----------------------------更新treeView資料--------------------------------------
        lastest_data = datasource.lastest_datetime_data()               
        self.cpblTreeView.update_content(site_datas=lastest_data)

#-----------------------------接收輸入的資料，並查詢&更新TreeView--------------------------------------
    def on_key_release(self, event):
        search_entry = event.widget  
        #print(search_entry)    
        #使用者輸入的文字  
        input_word = search_entry.get()
        print(input_word)
        
        if input_word == '':                                          #如果是空的，就自動更新最新資料在TreeView
            lastest_data = datasource.lastest_datetime_data()
            self.cpblTreeView.update_content(lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_word)  #如果有輸入值，就把輸入的值傳回search_sitename中查詢，並傳回結果&更新TreeView 
            self.cpblTreeView.update_content(search_data)      

    #傳球員資料的值
    def Paly_info():
        info = cpblTreeView.selectionItem()
        name = info[3]
        return name
    
#-----------------------------主程式定期自動更新資料--------------------------------------
def main():     
    def update_data(w:Window)->None:   
        datasource.update_sqlite_data()
        #-----------------------------更新treeView資料--------------------------------------
        latest_data = datasource.lastest_datetime_data()    #呼叫資料接收
        w.cpblTreeView.update_content(latest_data)
        print('資訊更新')

    window = Window() 
    window.title('中華職棒球員資料查詢')
    window.resizable(width=True,height=True) 
    update_data(window)
    window.mainloop() 

if __name__ == '__main__':
    main()