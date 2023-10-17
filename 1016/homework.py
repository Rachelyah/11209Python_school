'''
1. 下載台灣股市資訊
2. 存成csv檔案
3. 視窗樹狀表格(所有)
4. 當點選特定資料時，可以顯示點選欄位的詳細資訊
'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電2023年股票查詢")

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)
        
        #建立三個欄位，show='headings' 顯示最上面
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="Adj Close")
        self.tree.heading('#7', text="Volume")

        contacts = [] #建立一個空的list
        for n in range(1,100): #在n裡面依照順序放入1~100的數列
            #contacts.append([f'first {n}',f'last {n}',f'email{n}:example.com']) 
           #把n的資料分成三組資料存入list，每一筆資料會長這樣 ['first 22', 'last 22', 'email22:example.com']
           #會自動執行99次，建立99個list

        for contact in contacts: 
            self.tree.insert('',tk.END,value=contact)
            #再每一筆資料的結尾新增空字串(空一行)
        
        self.tree.pack() #反正一定要寫pack才會把內容顯示出來


def main():    
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()