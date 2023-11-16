import datasource
import psycopg2
import render_password as rpw
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbikeTreeView import youbikeTreeView
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義class的屬性
        super().__init__(**kwargs) #繼承原本Tk的屬性(self不用寫)
    #------------------------視窗介面----------------------------
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)
         #------------------------建立搜尋--------------------------------------
    #建立容器元素
        middleFrame = ttk.LabelFrame(self,text='',relief=tk.GROOVE,borderwidth=1)
        
    #建立標籤
        tk.Label(middleFrame,text='站點名稱搜尋').pack(side='left')
        
    #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.on_key_release)
        #透過bind註冊事件，當輸入發生時啟動on_key_release方法
        search_entry.pack(side='left')     
        middleFrame.pack(fill='x',padx=20)

    #------------------------------建立treeView-------------------------
        bottomFrame = tk.Frame(self)
        self.youbikeTreeView = youbikeTreeView(bottomFrame
                                                ,columns=('sna','mday','sarea','ar','tot', 'sbi', 'bemp')
                                                ,show="headings"
                                                ,height=20) #height的單位是行數的概念，注意不要太大
        #設定捲動軸 
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20)

    #-----------------------------接收輸入的資料，並查詢&更新TreeView--------------------------------------
    def on_key_release(self, event):
        search_entry = event.widget                                   #接收event儲存的entry資料，並使用widget取出值
        #print(search_entry)    
        #使用者輸入的文字  
        input_word = search_entry.get()
        print(input_word)
        if input_word == "":                                          #如果是空的，就自動更新最新資料在TreeView
            lastest_data = datasource.lastest_datetime_data()
            self.youbikeTreeView.update_content(lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_word)  #如果有輸入值，就把輸入的值傳回search_sitename中查詢，並傳回結果&更新TreeView 
            self.youbikeTreeView.update_content(search_data)

def main():
    def update_data(w:Window)->None:   
        #-----------------------------更新treeView資料--------------------------------------
        #------------------必須先顯示treeView資料，在更新最新資料內容，因為更新資料的時間太久--
        
        try:
            datasource.update_render_data()
            #pass
        except Exception: #當datasource傳出Exception
                          #套用messangebox.showerror方法，跳出另一個視窗呈現錯誤訊息
            messagebox.showerror('下載錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            #window.destroy() #自動關閉視窗

        latest_data = datasource.lastest_datetime_data()    #呼叫資料接收

        try:
            w.youbikeTreeView.update_content(latest_data)       #傳入Window裡

        except RuntimeError: #次執行中只會產生Runtime的錯誤
            return
        
        #-----------------------------更新treeView資料--------------------------------------
            
        #w.after(5*60*1000,update_data, w)  #每隔五分鐘更新一次
        t = Timer(5*60, update_data, args=(window,))
        t.start
        print('資訊更新')
        #after(self, ms, func=None， *args) 1000ms=1s
        #每隔五分鐘更新一次

    global t, window
    window = Window()             
    window.title('台北市youbike2.0')   
    #window.geometry('600x300')
    window.resizable(width=False ,height=False) 
    window.protocol("WM_DELETE_WINDOW", on_closing) #註冊當視窗關閉時，執行on_closing動作

    latest_data = datasource.lastest_datetime_data()    #呼叫資料接收
    window.youbikeTreeView.update_content(latest_data)       #傳入Window裡          
    
    #window.after(1000,update_data, window) #在一秒後先讓這行執行->視窗會先出現
    t = Timer(1, update_data, args=(window,))
    t.start()
    window.mainloop()

def on_closing():
    datasource.threadRun = False
    window.destroy() 
    t.cancel()
    #停止Timer，小猴子不跑了 #只有要使用t，沒有要建立，不用寫global t

if __name__ == "__main__":
    main()