from tkinter import ttk
from tkinter.simpledialog import Dialog

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent
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

    #--------------bind button1-------------------------
        self.bind('<Button-1>',self.selectionItem)

    #-------------更新資料內容------------------------
    def update_content(self,site_datas):

        #必須先清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for index, site in enumerate(site_datas):
            self.insert('','end',text=f'abc{index}',values=site)

    #點擊按鈕時，啟動此方法，print出資料內容，不用另外去資料庫找
    def selectionItem(self, event):
       selectedItem = self.focus()
       print(selectedItem)
       print(self.item(selectedItem))
       get_password = GetPassword(self.parent)

class GetPassword(Dialog):
    pass