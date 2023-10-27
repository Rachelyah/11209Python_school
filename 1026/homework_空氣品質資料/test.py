'''
下載台鐵即時列車資訊
'''

import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except Exception: 
            messagebox.showerror('下載錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() #自動關閉視窗

t=None 
def main():  
    def on_closing():             
        print('window關閉')
        t.cancel()                  
        window.destroy()    

#更新資料的function
    def update_data()->None:
        datasource.update_sqlite_data()
        print('資訊更新')
        global t                  
        t = Timer(60, update_data) 
        t.start()    

    window = Window()         
    window.title('台鐵即時列車資訊') 
    window.geometry('600x300')       
    window.resizable(width=False ,height=False) 
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()   

if __name__ == '__main__':
    main()