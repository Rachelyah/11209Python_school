import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        #self.geometry("300x250") #一般視窗都不會設大小，會用內容去撐開

class MyFrame(ttk.LabelFrame): #跟tk的Frame不一樣，多可以用text寫說明的功能
    def __init__(self,master, title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both', padx=10, pady=10)

        #會員登入標題(column橫跨兩欄)
        heading = ttk.Label(self, text="會員登入", font=('Helvetica', 20), foreground='blue')
        heading.grid(column=0, row=0, columnspan=2, padx=(20, 0)) #columnspan=一次橫跨多欄位

        #使用者名稱
        username_label = ttk.Label(self, text="使用者名稱:", font=('Helvetica', 12), foreground='black')
        username_label.grid(column=0,row=1,pady=10, padx=(10,0)) #距離左側10px，距離右側1px

        #輸入使用者名稱欄位
        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=1, padx=(0,10))

        #輸入密碼欄位
        password_label = ttk.Label(self, text="密碼:", font=('Helvetica', 12), foreground='black')
        password_label.grid(column=0, row=2, sticky=tk.E, padx=(10,1))
        password_entry = ttk.Entry(self, show='*') #讓輸入的密碼以*呈現
        password_entry.grid(column=1, row=2, padx=(0,10),pady=(0,20))

        #登入按鈕
        login_button = ttk.Button(self, text="登入",)
        login_button.grid(column=1, row=3, sticky=tk.E, padx=(0,10),pady=10)
        


def main():    
    window = Window()
    myFrame = MyFrame(window, "對齊方式")
    window.mainloop()

if __name__ == "__main__":
    main()