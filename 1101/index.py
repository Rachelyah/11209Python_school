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

        bottomFrame = tk.Frame(self)
#------------------------------建立treeView-----------------------------------------
        #建立treeView，記得要先建立View再放入資料，因為資料會一直更新
        #寫self代表未來它可以被其他的def呼叫
        self.tree = ttk.Treeview(bottomFrame, columns=('sna','sarea','mday','ar','tot', 'sbi', 'bemp'))  
        self.tree.heading('sna', text="站點名稱")
        self.tree.heading('sarea', text="行政區")
        self.tree.heading('mday', text="更新時間")
        self.tree.heading('ar', text="地址")
        self.tree.heading('tot', text="總車輛數")
        self.tree.heading('sbi', text="可借")
        self.tree.heading('bemp', text="可還")
        self.tree.pack()
        bottomFrame.pack(pady=15)
        
def main():     
#更新資料的function
    def update_data(w:Window)->None:    
        DataSource.update_sqlite_data()
        print('資訊更新')
        window.after(3*60*1000,update_data, w) #after(self, ms, func=None， *args) 1000ms=1s

    window = Window()               #建立一個window執行Window()
    window.title('台北市youbike2.0')    #設定視窗的title
    #window.geometry('600x300')          #設定視窗大小
    window.resizable(width=True ,height=True) #設定可開放調整視窗大小
    update_data(window)
    window.mainloop()               #永遠執行視窗，直到使用者下一個動作

if __name__ == '__main__':
    main()