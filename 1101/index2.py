'''
下載台北市youbike2.0的資料
'''

#將tkinter的包裹取名為tk
#tkinter裡面有很多package裡面有class
#tkinter裡面有一個class叫TK，包含所有視窗的功能

import tkinter as tk
from tkinter import ttk
import DataSource
from tkinter import messagebox
from threading import Timer
import YoubikeTreeView
from tkinter.simpledialog import Dialog

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

#-----------------------------建立查詢介面------------------------------------------
        middleFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(middleFrame,text='站點查詢').pack()
        tk.Label(middleFrame,text='請輸入第一階段關鍵字').pack()
        self.e = tk.StringVar()
        entryone = tk.Entry(middleFrame,textvariable=self.e)
        entryone.pack()
        
        '''
        #第一階段搜尋
        def search_stepone()->list:
            rows = (DataSource.search_sitename(entryone.get()))
            print(rows)
            return rows

        def clear():
            entryone.delete(0,tk.END)

        btn_search = tk.Button(middleFrame,text='搜尋',command=search_stepone).pack(side='left')
        btn_clear = tk.Button(middleFrame,text='清除',command=clear).pack(side='right')

        #第二階段搜尋
        tk.Label(middleFrame,text='請輸入進階搜尋關鍵字').pack()
        entrytwo = tk.Entry(middleFrame)
        entrytwo.pack()

        def search_steptwo():
            rows = search_stepone()
            print(rows)
            search = []
            if entrytwo.get() in rows:
                    search.append(rows)
            print(search)
            return search

        def clear():
            entrytwo.delete(0,tk.END)

        btn_search = tk.Button(middleFrame,text='搜尋',command=search_steptwo).pack(side='left')
        btn_clear = tk.Button(middleFrame,text='清除',command=clear).pack(side='right')
        
        '''
        middleFrame.pack()

#------------------------------建立treeView-----------------------------------------
#另外寫一個YoubikeTreeView模組，把TreeView設定寫在模組裡，再回來呼叫+pack
#建立treeView，記得要先建立View再放入資料，因為資料會一直更新
#寫self代表未來它可以被其他的def呼叫
        bottomFrame = tk.Frame(self)
        self.youbikeTreeView = YoubikeTreeView.YoubikeTreeView(bottomFrame
                                                               ,columns=('sna','sarea','mday','ar','tot', 'sbi', 'bemp')
                                                               ,show="headings"
                                                               ,height=20) #height的單位是行數的概念，注意不要太大
        #設定捲動軸 
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=30, padx=20)
        

#-----------------------------更新treeView資料--------------------------------------
        #lastest_data = DataSource.lastest_datetime_data()   #呼叫資料庫中最新的資料，用lastest_data接收
        #self.youbikeTreeView.update_content(site_datas=lastest_data) #傳入treeView的method中
        
def main():     
#更新資料的function
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