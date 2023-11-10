'''
下載台北市youbike2.0的資料
'''

#將tkinter的包裹取名為tk
#tkinter裡面有很多package裡面有class
#tkinter裡面有一個class叫TK，包含所有視窗的功能

import tkinter as tk
from tkinter import ttk
from YoubikeTreeView import youbikeTreeView
from tkinter import messagebox
from threading import Timer
import DataSource



class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義class的屬性
        super().__init__(**kwargs) #繼承原本Tk的屬性(self不用寫)
        try:
            DataSource.update_sqlite_data()
        except Exception: #當datasource傳出Exception
                          #套用messangebox.showerror方法，跳出另一個視窗呈現錯誤訊息
            messagebox.showerror('下載錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() #自動關閉視窗

#-------------------------------建立介面--------------------------------------------
#print(DataSource.lastest_datetime_data())
        #最上面的視窗topFrame，設定rekief視窗樣式
        topFrame =tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        #只要裡面有內容，topFrame的邊框&預設大小就會失效，除非下Label的邊框距離設定
        #建立Label標籤放在topFrame裡面，設定與邊框的距離
        tk.Label(topFrame,text='台北市youbike即時資料',font=('arial,30'),bg='#333333',fg='#FFFFFF',pady=20).pack(pady=20, padx=20)  
        topFrame.pack(pady=30)

#-----------------------------建立查詢介面(老師的答案)------------------------------------------
        #建立容器元素
        middleFrame = ttk.LabelFrame(self,text='',relief=tk.GROOVE,borderwidth=1)
        
        
        #建立標籤
        tk.Label(middleFrame,text='站點名稱搜尋').pack(side='left')
        
        #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.on_key_release)  #透過bind註冊事件，當輸入發生時啟動on_key_release方法
        search_entry.pack(side='left')     
        middleFrame.pack(fill='x',padx=20)
        #不能直接.pack，執行初始化會直接傳出None，必須先得到實體再做pack
        #判斷能不能直接.pack()，你前面的東西是不是一個實體
        #search_entry的東西，我未來還會呼叫使用，所以我先傳入self.search_entry裡，而傳入之後我的tk.Entry()就會變成None，如果直接pack就會是None

        #註冊輸入事件並設定傳回接收位置
        #使用者每打一個字(在python的世界被稱為「一個事件」)，我希望他回傳到我這，這時我就必須用StringVar儲存隨時會變動的字串值，並且搭配bind控制每次事件發生時，我都可以接收到事件內容
        
#------------------------------建立treeView-----------------------------------------
#另外寫一個YoubikeTreeView模組，把TreeView設定寫在模組裡，再回來呼叫+pack
#建立treeView，記得要先建立View再放入資料，因為資料會一直更新
#寫self代表未來它可以被其他的def呼叫
        bottomFrame = tk.Frame(self)
        self.youbikeTreeView = youbikeTreeView(bottomFrame
                                                               ,columns=('sna','sarea','mday','ar','tot', 'sbi', 'bemp')
                                                               ,show="headings"
                                                               ,height=20) #height的單位是行數的概念，注意不要太大
        #設定捲動軸 
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20) #pady=(與上段距離，與下段距離)
        

#-----------------------------更新treeView資料--------------------------------------
        lastest_data = DataSource.lastest_datetime_data()               #呼叫資料庫中最新的資料，用lastest_data接收
        self.youbikeTreeView.update_content(site_datas=lastest_data)    #傳入treeView的method中

#-----------------------------接收輸入的資料，並查詢&更新TreeView--------------------------------------
    def on_key_release(self, event):
        search_entry = event.widget                                   #接收event儲存的entry資料，並使用widget取出值
        #print(search_entry)    
        #使用者輸入的文字  
        input_word = search_entry.get()
        print(input_word)
        if input_word == '':                                          #如果是空的，就自動更新最新資料在TreeView
            lastest_data = DataSource.lastest_datetime_data()
            self.youbikeTreeView.update_content(lastest_data)
        else:
            search_data = DataSource.search_sitename(word=input_word)  #如果有輸入值，就把輸入的值傳回search_sitename中查詢，並傳回結果&更新TreeView 
            self.youbikeTreeView.update_content(search_data)

#-----------------------------主程式定期自動更新資料--------------------------------------
def main():     
    def update_data(w:Window)->None:   
        DataSource.update_sqlite_data()
        #-----------------------------更新treeView資料--------------------------------------
        latest_data = DataSource.lastest_datetime_data()    #呼叫資料接收
        w.youbikeTreeView.update_content(latest_data)       #傳入Window裡
        print('資訊更新')
        window.after(3*60*1000,update_data, w) #after(self, ms, func=None， *args) 1000ms=1s
        #每隔三分鐘更新一次

    window = Window()               #建立一個window執行Window()
    window.title('台北市youbike2.0')    #設定視窗的title
    window.resizable(width=False ,height=False) #設定可開放調整視窗大小
    update_data(window)
    window.mainloop()               #永遠執行視窗，直到使用者下一個動作

if __name__ == '__main__':
    main()