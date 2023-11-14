from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog

class pm25_treeview(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent
        #------設定欄位名稱---------------
        self.heading('site',text='測站名稱')
        self.heading('county',text='縣市名稱')
        self.heading('pm25',text='細懸浮微粒濃度')
        self.heading('datacreationdate',text='資料建置時間')

        #----------設定欄位寬度------------
        self.column('site',width=250)
        self.column('county',width=250)
        self.column('pm25',width=200)
        self.column('datacreationdate',width=300)

        #----------註冊按鈕：當使用者點擊時觸發-------
        self.bind('<ButtonRelease-1>', self.selectedItem)

#----------當使用者輸入搜尋時更新treeview中資料--------
    def update_content(self,site_datas):
        #清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for index,site in enumerate(site_datas):
            self.insert('','end',text=f"abc{index}",values=site)

#---------當使用者輸入搜尋時觸發此方法-----------  
    def selectedItem(self,event):
        selectedItem = self.focus()
        print(selectedItem)
        data_dict = self.item(selectedItem)
        data_list = data_dict['values']
        title = data_list[0]
        detail = ShowDetail(self.parent,data=data_list,title=title)

#抓取使用者輸入的資料查詢結果
class ShowDetail(Dialog):
    def __init__(self,parent,data,**kwargs):
        self.site = data[0]
        self.county = data[1]
        self.pm25 = data[2]
        self.datacreationdate = data[3]
        super().__init__(parent,**kwargs)

    #設定使用者點選時彈出視窗呈現詳細資訊   
    def body(self, master):        
        '''
        override body,可以自訂body的外觀內容
        '''
        mainFrame = tk.Frame(master)
        mainFrame.pack(padx=100,pady=100)
        tk.Label(mainFrame,text="測站名稱", pady=5).grid(column=0, row=0)
        tk.Label(mainFrame,text="縣市名稱", pady=5).grid(column=0, row=1)
        tk.Label(mainFrame,text="細懸浮微粒濃度", pady=5).grid(column=0, row=2)
        tk.Label(mainFrame,text="資料建置時間", pady=5).grid(column=0, row=3)

        siteVar = tk.StringVar()
        siteVar.set(self.site)
        tk.Entry(mainFrame,textvariable=siteVar,state='disabled',width=40,justify='center').grid(column=1,row=0)

        countyVar = tk.StringVar()
        countyVar.set(self.county)
        tk.Entry(mainFrame,textvariable=countyVar,state='disabled',width=40,justify='center').grid(column=1,row=1)

        pm25Var = tk.StringVar()
        pm25Var.set(self.pm25)
        tk.Entry(mainFrame,textvariable=pm25Var,state='disabled',width=40,justify='center').grid(column=1,row=2)

        dateVar = tk.StringVar()
        dateVar.set(self.datacreationdate)
        tk.Entry(mainFrame,textvariable=dateVar,state='disabled',width=40,justify='center').grid(column=1,row=3)


    def buttonbox(self):
        '''
        override buttonbox,可以自訂body的外觀內容
        '''
        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(padx=5, pady=(5,20))      

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()