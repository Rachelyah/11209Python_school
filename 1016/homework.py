'''
1. 下載台灣股市資訊
2. 存成csv檔案
3. 視窗樹狀表格(所有)
4. 當點選特定資料時，可以顯示點選欄位的詳細資訊
'''

import datasource
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電2023年股票查詢")

class GetPassword(Dialog):
    def body(self, master): 
        self.title("Enter New Password")
        tk.Label(master, text='Date:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='Open:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='High:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='Low:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='Close:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='Adj Close:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='Volume:').grid(row=6, sticky=tk.W)

        #從動態字串中叫出資料
        self.DateVar = tk.StringVar()
        tk.Label(master, textvariable=self.DateVar).grid(column=0, sticky=tk.W)

        self.OpenVar = tk.StringVar()
        tk.Label(master, textvariable=self.OpenVar).grid(column=1, sticky=tk.W)

        self.HighVar = tk.StringVar()
        tk.Label(master, textvariable=self.HighVar).grid(row=2, sticky=tk.W)

        self.LowVar = tk.StringVar()
        tk.Label(master, textvariable=self.LowVar).grid(row=3, sticky=tk.W)

        self.CloseVar = tk.StringVar()
        tk.Label(master, textvariable=self.CloseVar).grid(row=4, sticky=tk.W)

        self.Adj_CloseVar = tk.StringVar()
        tk.Label(master, textvariable=self.Adj_CloseVar).grid(row=5, sticky=tk.W)

        self.VolumeVar = tk.StringVar()
        tk.Label(master, textvariable=self.VolumeVar).grid(row=6, sticky=tk.W)
'''
        data = datasource.csv_data()
        self.DateVar.set(data[0])
        self.OpenVar.set(data[1])
        self.HighVar.set(data[2])
        self.LowVar.set(data[3])
        self.CloseVar.set(data[4])
        self.Adj_CloseVar.set(data[5])
        self.VolumeVar.set(data[6])
'''

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="Adj Close")
        self.tree.heading('#7', text="Volume")

        with open('yf_2330.csv') as data:
            data = csv.DictReader(data)
            for row in data: 
                Date = row['Date']
                Open = row['Open']
                High = row['High']
                Low = row['Low']
                Close = row['Close']
                Adj_Close = row['Adj Close']
                Volume = row['Volume']
                self.tree.insert('',tk.END,value=(Date, Open, High, Low, Close, Adj_Close, Volume))

        #新增垂直卷軸
        #scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
        #tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')


        self.tree.pack() 
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)

    def item_selected(self, event):
        item_id = self.tree.selection()[0] 
        self.tree.item(item_id)
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])

'''
        self.OpenVar.set(data[1])
        self.HighVar.set(data[2])
        self.LowVar.set(data[3])
        self.CloseVar.set(data[4])
        self.Adj_CloseVar.set(data[5])
        self.VolumeVar.set(data[6])
        dialog = GetPassword(self)
'''
        
def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電2023年股票查詢")  
    window.mainloop()

if __name__ == "__main__":
    main()