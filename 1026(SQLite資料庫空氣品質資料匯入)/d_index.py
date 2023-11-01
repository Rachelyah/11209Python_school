'''
下載台北市youbike2.0的資料
'''

#將tkinter的包裹取名為tk
#tkinter裡面有很多package裡面有class
#tkinter裡面有一個class叫TK，包含所有視窗的功能

import tkinter as tk
from tkinter import ttk
import d_datasource
from tkinter import messagebox

class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義class的屬性
        super().__init__(**kwargs) #繼承原本Tk的屬性(self不用寫)
        try:
            d_datasource.update_sqlite_data()
        except Exception: #當datasource傳出Exception(錯誤訊息時，)
            #套用messangebox.showerror方法，跳出另一個視窗呈現錯誤訊息
            messagebox.showerror('下載錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() #自動關閉視窗

def main():
    window = Window() #建立一個window執行Window()
    window.title('台北市youbike2.0') #設定視窗的title
    window.geometry('600x300') #設定視窗大小
    window.resizable(width=False ,height=False) #固定視窗大小
    window.mainloop() #永遠執行視窗，直到使用者下一個動作

if __name__ == '__main__':
    main()