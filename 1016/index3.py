#設定radiobutton，並設定預設值

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#E79460')

class MyFrame(ttk.LabelFrame): #跟tk的Frame不一樣，多可以用text寫說明的功能
    def __init__(self,master, title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        #self.configure(background='#9E7A7A')
        #ttk不能用背景色，ttk類似css的用法
        self.aligement = tk.StringVar(value='center') #預設值是中間
        ttk.Radiobutton(self, text="左邊", variable=self.aligement, command=self.choised, value='left').grid(column=0,row=0, padx=10) #要寫variable這個變數，儲存預設值，並寫在rariobutton中連結(每個選項都要寫)
        ttk.Radiobutton(self, text="中間", variable=self.aligement, command=self.choised, value='center').grid(column=1,row=0, padx=10)
        ttk.Radiobutton(self, text="右邊", variable=self.aligement, command=self.choised, value='right').grid(column=2,row=0, padx=10) 
        self.pack(expand=1, fill='x', padx=10, pady=10)

    #自動print出使用者選擇的value
    def choised(self): #不需要給參數，bind才必要
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window, "對齊方式")
    window.mainloop()

if __name__ == "__main__":
    main()