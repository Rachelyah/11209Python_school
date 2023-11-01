from tkinter import ttk

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
    #--------------設定欄位名稱--------------------
        self.heading('sna', text="站點名稱")
        self.heading('sarea', text="行政區")
        self.heading('mday', text="更新時間")
        self.heading('ar', text="地址")
        self.heading('tot', text="總車輛數")
        self.heading('sbi', text="可借")
        self.heading('bemp', text="可還")
    #--------------設定欄位寬度-----------------------
        self.column('sna',width=250) #也可以用minwidth設定最小寬度
        self.column('sarea',width=120)
        self.column('mday',width=250)
        self.column('ar',width=280)
        self.column('tot',width=100)
        self.column('sbi',width=80)
        self.column('bemp',width=80)

    #-------------更新資料內容------------------------
    def update_content(self,site_datas):
        #必須先清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for site in site_datas:
            self.insert('','end',values=site)