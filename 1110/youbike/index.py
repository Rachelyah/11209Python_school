import datasource
import psycopg2
import password as pw
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbikeTreeView import YoubikeTreeView
from threading import Timer
from threading import Thread
import time

'''
解決視窗結束時，主程式執行無法中止的問題：

*datasource
1. 給一個全域變數threadRun=True
2. 在insert data的for迴圈前，判斷threadRun=True才執行insert，若是False就停止執行

*index.py
1. 註冊視窗關閉時的動作 window.protocol("WM_DELETE_WINDOW", on_closing)
2. 在on_closing中，放入datasource.threadRun = False，傳回datasource
3. 其中更新treeView資訊的方法 w.youbikeTreeView.update_content(lastest_data) 在關閉視窗之後會出現錯誤，寫入try&excpet條件，當發生錯誤時，傳回空值



'''

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------建立介面------------------------
        #print(datasource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)
        #---------------------------------------

        #----------建立搜尋------------------------
        middleFrame = ttk.LabelFrame(self,text='')
        tk.Label(middleFrame,text='站點名稱搜尋:').pack(side='left')
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.OnEntryClick)
        search_entry.pack(side='left')        
        middleFrame.pack(fill='x',padx=20)
        #----------------------------------------

        #---------------建立treeView---------------
        bottomFrame = tk.Frame(self)
        
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",
                                               columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                                               height=20)
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30),padx=20)
        #-------------------------------------------

    def OnEntryClick(self,event):
        searchEntry = event.widget
        #使用者輸入的文字
        input_word = searchEntry.get()
        if input_word == "":
            lastest_data = datasource.lastest_datetime_data()
            self.youbikeTreeView.update_content(lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_word)
            self.youbikeTreeView.update_content(search_data)

def main():
    def update_data(w:Window)->None:
        #-----------更新treeView資料---------------
        global t #global t 一般都寫在function最上面
        try:
            datasource.updata_render_data()
            #pass
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            #window.destroy()

        lastest_data = datasource.lastest_datetime_data()
        
        try :
            w.youbikeTreeView.update_content(lastest_data)
        
        #RuntimeError：代表程式在執行過程(runtime)中出現錯誤，當發生此錯誤時直接return不傳回東西，並結束這個地方的執行，不耽誤其他程式的執行
        except RuntimeError: #次執行中只會產生Runtime的錯誤
            return
        
        
        #w.after(5*60*1000,update_data,w) #每隔5分鐘
        t = Timer(5*60, update_data,args=(window,))
        t.start()

    global t, window
    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    window.protocol("WM_DELETE_WINDOW", on_closing) #註冊當視窗關閉時，執行on_closing動作
    lastest_data = datasource.lastest_datetime_data()
    window.youbikeTreeView.update_content(lastest_data)
    #window.after(1000,update_data,window) 
    t = Timer(1, update_data,args=(window,))
    #t = Thread(target=update_data, args=(window,5*60))
    t.start()         
    window.mainloop()
    
def on_closing():
    datasource.threadRun = False
    window.destroy() 
    t.cancel()
    #停止Timer，小猴子不跑了 #只有要使用t，沒有要建立，不用寫global t
    

if __name__ == "__main__":
    t= None #聲明變數的類型提示，是一個用到Thread類型的變數，可寫可不寫
    window= None
    main()