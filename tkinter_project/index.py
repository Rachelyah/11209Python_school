'''
cpbl
'''

import tkinter as tk
from tkinter import ttk
from cpbl_treeview import cpblTreeView, Player_info, player
from tkinter import messagebox
from threading import Timer
import datasource
from PIL import Image, ImageTk

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
        middleFrame = ttk.LabelFrame(self,text='球員搜尋',relief=tk.GROOVE,borderwidth=1)
        
        #建立標籤
        #tk.Label(middleFrame).pack(side='top')

        #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.on_key_release)
        search_entry.pack()     
        middleFrame.pack()

#------------------------------球員個人資料、PR數據---------------------------------------
        
        self.tk_img = None
        photoFrame = ttk.LabelFrame(self,text='球員照片',relief=tk.GROOVE,borderwidth=1)
        photoFrame.pack(side='left', anchor="n", expand=True, padx=5, pady=5, ipadx=5, ipady=5)
        self.tk_img = None
        #self.show_image(photoFrame)
        
    
    def show_image(self, frame):    
        name = player.player_name()
        photo_path = f'./img/{name}.jpg'
        img = Image.open(photo_path)

        # 調整圖片大小為 120x160，注意這裡的尺寸修改
        img = img.resize((120, 160), Image.BILINEAR)

        # 將圖片轉換為 Tkinter PhotoImage 對象，使用實例變數
        self.tk_img = ImageTk.PhotoImage(img)

        # 創建一個 Canvas 並在其中放入圖片
        canvas = tk.Canvas(frame, width=120, height=160)
        canvas.create_image(0, 0, anchor='nw', image=self.tk_img)
        canvas.pack()

        # 將 infoFrame 放入同一個父容器（一個新的 Frame）中
        container_frame = tk.Frame(frame)
        container_frame.pack(side='left', anchor="n",fill='y', expand=True, padx=5, pady=5, ipadx=5, ipady=5)

        infoFrame = ttk.LabelFrame(container_frame, text='球員資料', relief=tk.GROOVE, borderwidth=1)
        infoFrame.pack(side='left', anchor="n", expand=True, padx=5, pady=5, ipadx=5, ipady=5)


        #infoFrame = ttk.LabelFrame(self,text='球員資料',relief=tk.GROOVE,borderwidth=1)
        #infoFrame.pack(side='left', anchor="n", expand=True, padx=5, pady=5, ipadx=5, ipady=5)

        def info(event):
            info =  Player_info.frame(infoFrame)
            
        
        #prFrame = ttk.LabelFrame(self,text='球員資料',relief=tk.GROOVE,borderwidth=1)
        #prlabel = tk.Label(prFrame, text='所屬球隊：')
        #prlabel.pack()
        #prFrame.pack(side='top',anchor="n", expand=True)
        
        btn = tk.Button(container_frame, text='球員資料查詢')
        #btn.pack(side='bottom', anchor="s", expand=True, padx=5, pady=5, ipadx=5, ipady=5)


        #info =  Player_info.frame(infoFrame)
        #btn.bind('<ButtonRelease-1>',info)

        '''
    #測試中：更新球員資料
    def update_player_photo(self, data):
        # data 中包含所選擇球員的相關資訊，例如姓名
        # 在這裡根據球員姓名找到照片的檔案路徑
        data = Player_info()
        player_name = data[3]  # 假設姓名在 data 中的第四個位置
        print(data)

        # 假設照片檔案放在 './img/' 資料夾下，檔案名稱為球員姓名加上 '.jpg'
        photo_path = f'./img/{player_name}.jpg'

        # 更新球員照片
        self.show_image(photo_path)
        '''

##-----------------------------建立隊伍按鈕-----------------------------------

        middle1Frame = ttk.LabelFrame(self,text='選擇球隊',relief=tk.GROOVE,borderwidth=1)
        tk.Label(middle1Frame,text='選擇球隊').pack
        middle1Frame.pack(side='top',fill='x', padx=20, pady=20, expand=True)

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
        self.cpblTreeView = cpblTreeView(bottomFrame,columns=('Year','Team Name','ID','Name','G', 'GS', 'GR', 'W', 'L', 'SV', 'HLD', 'IP', 'BF', 'H', 'HR', 'BB', 'SO', 'ER'),show="headings",height=20)
        #設定捲動軸 
        self.cpblTreeView.pack(side='top', fill='both', expand=True)
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.cpblTreeView.yview)
        vsb.pack(side='left',fill='y', expand=True)
        self.cpblTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20) #pady=(與上段距離，與下段距離)
        self.bind('<ButtonRelease-1>',info)
        
        
        
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