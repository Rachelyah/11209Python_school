import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

class youbikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):   
        super().__init__(parent,**kwargs) 
        self.parent = parent
    #--------------設定欄位名稱--------------------
        self.heading('sna', text="站點名稱")
        self.heading('mday', text="更新時間")
        self.heading('sarea', text="行政區")
        self.heading('ar', text="地址")
        self.heading('tot', text="總車輛數")
        self.heading('sbi', text="可借")
        self.heading('bemp', text="可還")
    #--------------設定欄位寬度-----------------------
        self.column('sna',width=250) #也可以用minwidth設定最小寬度
        self.column('mday',width=250)
        self.column('sarea',width=100)
        self.column('ar',width=280)
        self.column('tot',width=100)
        self.column('sbi',width=80)
        self.column('bemp',width=80)
        
    #--------------bind button1-------------------------
        self.bind('<ButtonRelease-1>',self.selectionItem)

    #-------------更新資料內容------------------------
    def update_content(self,site_datas):

        #必須先清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for index, site in enumerate(site_datas):
            self.insert('','end',text=f'abc{index}',values=site)

    #點擊按鈕時，啟動此方法，print出資料內容，不用另外去資料庫找
    def selectionItem(self, event):
       selectedItem = self.focus()      #抓出選擇的值
       print(selectedItem)                  
       data_dict = self.item(selectedItem)  #儲存抓出來的值(dict型別)
       #print(data_dict)
       data_list = data_dict['values']      #儲存Value值(list型別)
       print(data_list)
       title_name = data_list[0]            #抓出名稱放在title
       detail = ShowDetail(self.parent, data = data_list, title=title_name)    
       #呼叫ShowDetail並傳入parent(title)，並把我的data傳入

class ShowDetail(Dialog):
    def __init__(self,parent, data:list,**kwargs):    #定義，parent的是自訂的籃子，是呼叫時必要的參數，並加入data的參數需求(父類別沒有的)
        #把傳入的data資料傳給self.data(屬性)，這樣之後可以在這個class所有實體方法都可以使用
        self.sna = data[0]                    
        self.mday = data[1]
        self.sarea = data[2]
        self.ar = data[3]
        self.tot = data[4]
        self.sbi = data[5]
        self.bemp = data[6]
        super().__init__(parent, **kwargs)  #呼叫父類別的
        #print(data)

        #overridden def body：Dialog裡面有def body，但我把它複寫
        #以後呼叫body都以我的規定為主
        #如果父類別裡面有我要的東西，我子類別就要用super接收
        #但body的父類別裡面根本沒東西，所以我可以根本就不用super
    def body(self, master):
        #super().body(master)   #省略
        #init要寫在父容器master裡面

        #建立彈出視窗欄位（橫：row；直：column）
        mainFrame = tk.Frame(master)
        mainFrame.pack(padx=100,pady=100)
        tk.Label(mainFrame,text="站點名稱", pady=5).grid(column=0, row=0)
        tk.Label(mainFrame,text="更新時間", pady=5).grid(column=0, row=1)
        tk.Label(mainFrame,text="行政區", pady=5).grid(column=0, row=2)
        tk.Label(mainFrame,text="地址", pady=5).grid(column=0, row=3)
        tk.Label(mainFrame,text="總量", pady=5).grid(column=0, row=4)
        tk.Label(mainFrame,text="可借", pady=5).grid(column=0, row=5)
        tk.Label(mainFrame,text="可還", pady=5).grid(column=0, row=6)

        #建立欄位內容，內容文字為texrvariable=StringVar，用這個接收
        #state = disabled 不可被修改
        snaVar = tk.StringVar()
        snaVar.set(self.sna)
        tk.Entry(mainFrame,textvariable=snaVar, state='disabled',width=40,justify='center').grid(column=1,row=0)

        mdayVar = tk.StringVar()
        mdayVar.set(self.mday)
        tk.Entry(mainFrame,textvariable=mdayVar,state='disabled',width=40,justify='center').grid(column=1,row=1)

        sareaVar = tk.StringVar()
        sareaVar.set(self.sarea)
        tk.Entry(mainFrame,textvariable=sareaVar,state='disabled',width=40,justify='center').grid(column=1,row=2)

        arVar = tk.StringVar()
        arVar.set(self.ar)
        tk.Entry(mainFrame,textvariable=arVar,state='disabled',width=40,justify='center').grid(column=1,row=3)

        totVar = tk.StringVar()
        totVar.set(self.tot)
        tk.Entry(mainFrame,textvariable=totVar,state='disabled',width=40,justify='center').grid(column=1,row=4)

        sbiVar = tk.StringVar()
        sbiVar.set(self.sbi)
        tk.Entry(mainFrame,textvariable=sbiVar,state='disabled',width=40,justify='center').grid(column=1,row=5)

        bempVar = tk.StringVar()
        bempVar.set(self.bemp)
        tk.Entry(mainFrame,textvariable=bempVar,state='disabled',width=40,justify='center').grid(column=1,row=6)

# 複寫Dialog內建的def buttonbox
# 要super接收他的init，才會有OK跟cancel，如果沒有寫，就不會有
    def buttonbox(self):
        '''
        override buttonbox，可以自訂body的外觀內容
        '''
        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(padx=5, pady=(5,20)) #(對上的y距離，對下的y距離)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        
        box.pack()
    
    
   