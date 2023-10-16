#用Treeview建立樹視圖

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__( **kwargs) 
        self.title("Image")       

class MyFrame(ttk.LabelFrame): #跟tk的Frame不一樣，多可以用text寫說明的功能
    def __init__(self,master, title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both', padx=10, pady=10)
        
        #建立三個欄位
        self.tree = ttk.Treeview(self, columns=['#1', '#2', '#3'], show='headings') 
        self.tree.heading('#1', text='第一欄')
        self.tree.heading('#2', text='第二欄')
        self.tree.heading('#3', text='第三欄')

        contacts = []
        for n in range(1,100):
            contacts.append([f'first{n}', f'last{n}', f'email{n}:example.com'])
        
        for contact in contacts:
            self.tree.insert('',tk.END,value=contact)
        
        self.tree.pack()

def main():    
    window = Window()
    myFrame = MyFrame(window, "對齊方式")
    window.mainloop()

if __name__ == "__main__":
    main()