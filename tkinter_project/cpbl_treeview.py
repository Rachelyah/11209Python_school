import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import sqlite3

#index：創造母盒，呼叫cpbl的grid，包含左邊的欄位跟右邊的變數欄位
#cpbl：創建左邊欄位tk.Label，右邊的變數欄位（用sql語法查出結果）

t = [2022, '富邦', 363, '陳仕朋', 23, 18, 5, 8, 6, 0, 0, '113.2', 473, 108, 7, 37, 86, 34, '左投左打', 2022, '富邦', 363, '陳仕朋', 23, 18, 5, 8, 6, 0, 0, '113.2', 473, 108, 7, 37, 86, 34, '左投左打']
class cpblTreeView(ttk.Treeview, tk.Frame):

    def __init__(self,parent,**kwargs):   
        super().__init__(parent,**kwargs) 
        self.parent = parent
        self.heading('Year', text="年份")
        self.heading('Team Name', text="所屬球隊")
        self.heading('ID', text="球員編號")
        self.heading('Name', text="球員姓名")
        self.heading('G', text="出場數")
        self.heading('GS', text="先發次數")
        self.heading('GR', text="中繼次數")
        self.heading('W', text="勝場數")
        self.heading('L', text="敗場數")
        self.heading('SV', text="救援成功")
        self.heading('HLD', text="中繼成功")
        self.heading('IP', text="有效局數")
        self.heading('BF', text="面對打者數")
        self.heading('H', text="被安打數")
        self.heading('HR', text="被全壘打數")
        self.heading('BB', text="保送數")
        self.heading('SO', text="三振數")
        self.heading('ER', text="自責分")
    
    #--------------設定欄位寬度-----------------------
        self.column('Year',width=70,anchor='center') #也可以用minwidth設定最小寬度
        self.column('Team Name',width=70,anchor='center')
        self.column('ID',width=100,anchor='center')
        self.column('Name',width=70,anchor='center')
        self.column('G',width=70,anchor='center')
        self.column('GS',width=70,anchor='center')
        self.column('GR',width=70,anchor='center')
        self.column('W',width=70,anchor='center')
        self.column('L',width=70,anchor='center')
        self.column('SV',width=70,anchor='center')
        self.column('HLD',width=70,anchor='center')
        self.column('IP',width=70,anchor='center')
        self.column('BF',width=70,anchor='center')
        self.column('H',width=70,anchor='center')
        self.column('HR',width=70,anchor='center')
        self.column('BB',width=70,anchor='center')
        self.column('SO',width=70,anchor='center')
        self.column('ER',width=70,anchor='center')

    #--------------bind button1-------------------------
        self.bind('<ButtonRelease-1>',self.selectionItem)

    #-------------更新資料內容------------------------
    def update_content(self,site_datas):
        #必須先清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for index, site in enumerate(site_datas):
            self.insert('','end',text=f'abc{index}' ,values=site)
        

    #點擊treeView時，啟動此方法，回傳使用者點擊資料
    def selectionItem(self, event)->list:
       global t
       selectedItem = self.focus()
       data_dict = self.item(selectedItem)
       t = data_dict['values']
       print(f'selectionItem查詢結果{t}')
       #info = Player_info.frame(t)

       #將資料傳入彈出視窗
       title_name = t[0]
       detail = ShowDetail(self.parent, data=t, title=title_name)

       data = Player_info.frame(t)

       return t

class ShowDetail(Dialog):
    def __init__(self,parent, data:list,**kwargs):
        self.Year = data[0]                    
        self.Team = data[1]
        self.ID = data[2]
        self.Name = data[3]
        self.G = data[4]
        self.GS = data[5]
        self.GR = data[6]
        self.W = data[7]                    
        self.L = data[8]
        self.SV = data[9]
        self.HLD = data[10]
        self.IP = data[11]
        self.BF = data[12]
        self.H = data[13]
        self.HR = data[14]                    
        self.BB = data[15]
        self.SO = data[16]
        self.ER = data[17]
        super().__init__(parent, **kwargs)  

    def body(self, master):
        mainFrame= tk.Frame(master)
        mainFrame.pack(padx=100, pady=100) 

        #建立彈出視窗欄位（橫：row；直：column）
        tk.Label(mainFrame, text='年份').grid(column=0, row=0)
        tk.Label(mainFrame, text='所屬球隊').grid(column=0, row=1)
        tk.Label(mainFrame, text='球員編號').grid(column=0, row=2)
        tk.Label(mainFrame, text='球員姓名').grid(column=0, row=3)
        tk.Label(mainFrame, text='出場數').grid(column=0, row=4)
        tk.Label(mainFrame, text='先發次數').grid(column=0, row=5)
        tk.Label(mainFrame, text='中繼次數').grid(column=0, row=6)
        tk.Label(mainFrame, text='勝場數').grid(column=0, row=7)
        tk.Label(mainFrame, text='敗場數').grid(column=0, row=8)
        tk.Label(mainFrame, text='救援成功').grid(column=0, row=9)
        tk.Label(mainFrame, text='中繼成功').grid(column=0, row=10)
        tk.Label(mainFrame, text='有效局數').grid(column=0, row=11)
        tk.Label(mainFrame, text='面對打者數').grid(column=0, row=12)
        tk.Label(mainFrame, text='被安打數').grid(column=0, row=13)
        tk.Label(mainFrame, text='被全壘打數').grid(column=0, row=14)
        tk.Label(mainFrame, text='保送數').grid(column=0, row=15)
        tk.Label(mainFrame, text='三振數').grid(column=0, row=16)
        tk.Label(mainFrame, text='自責分').grid(column=0, row=17)

        #建立欄位內容，內容文字為texrvariable=StringVar，用這個接收
        #state = disabled 不可被修改
        YearVar = tk.StringVar()
        YearVar.set(self.Year)
        tk.Entry(mainFrame,textvariable=YearVar, state='disabled').grid(column=1,row=0)

        TeamVar = tk.StringVar()
        TeamVar.set(self.Team)
        tk.Entry(mainFrame,textvariable=TeamVar, state='disabled').grid(column=1,row=1)

        IDVar = tk.StringVar()
        IDVar.set(self.ID)
        tk.Entry(mainFrame,textvariable=IDVar, state='disabled').grid(column=1,row=2)

        NameVar = tk.StringVar()
        NameVar.set(self.Name)
        tk.Entry(mainFrame,textvariable=NameVar, state='disabled').grid(column=1,row=3)

        GVar = tk.StringVar()
        GVar.set(self.G)
        tk.Entry(mainFrame,textvariable=GVar, state='disabled').grid(column=1,row=4)

        GSVar = tk.StringVar()
        GSVar.set(self.GS)
        tk.Entry(mainFrame,textvariable=GSVar, state='disabled').grid(column=1,row=5)

        GRVar = tk.StringVar()
        GRVar.set(self.GR)
        tk.Entry(mainFrame,textvariable=GRVar, state='disabled').grid(column=1,row=6)

        WVar = tk.StringVar()
        WVar.set(self.W)
        tk.Entry(mainFrame,textvariable=WVar, state='disabled').grid(column=1,row=7)

        LVar = tk.StringVar()
        LVar.set(self.L)
        tk.Entry(mainFrame,textvariable=LVar, state='disabled').grid(column=1,row=8)

        SVVar = tk.StringVar()
        SVVar.set(self.SV)
        tk.Entry(mainFrame,textvariable=SVVar, state='disabled').grid(column=1,row=9)

        HLDVar = tk.StringVar()
        HLDVar.set(self.HLD)
        tk.Entry(mainFrame,textvariable=HLDVar, state='disabled').grid(column=1,row=10)

        IPVar = tk.StringVar()
        IPVar.set(self.IP)
        tk.Entry(mainFrame,textvariable=IPVar, state='disabled').grid(column=1,row=11)

        BFVar = tk.StringVar()
        BFVar.set(self.BF)
        tk.Entry(mainFrame,textvariable=BFVar, state='disabled').grid(column=1,row=12)

        HVar = tk.StringVar()
        HVar.set(self.H)
        tk.Entry(mainFrame,textvariable=HVar, state='disabled').grid(column=1,row=13)

        HRVar = tk.StringVar()
        HRVar.set(self.HR)
        tk.Entry(mainFrame,textvariable=HRVar, state='disabled').grid(column=1,row=14)

        BBVar = tk.StringVar()
        BBVar.set(self.BB)
        tk.Entry(mainFrame,textvariable=BBVar, state='disabled').grid(column=1,row=15)

        SOVar = tk.StringVar()
        SOVar.set(self.SO)
        tk.Entry(mainFrame,textvariable=SOVar, state='disabled').grid(column=1,row=16)

        ERVar = tk.StringVar()
        ERVar.set(self.ER)
        tk.Entry(mainFrame,textvariable=ERVar, state='disabled').grid(column=1,row=17)


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
        box.pack()


class Player_info(tk.Tk):
    #問題出在這！！！！！！！！！
    def frame(self,**kwargs):
        print(f'走到frame{t}')
        print(type(t))

        Team = t[1]
        Name = t[3]
        B_t = t[18]                 
        Number = t[19]
        Ht_wt = t[20]
        Born = t[21]
        print(f'生日{Born}')

        self.Team = tk.Label(self, text='所屬球隊：').grid(row=0, column=0, sticky='w')
        self.Name = tk.Label(self, text='球員姓名：').grid(row=1, column=0, sticky='w')
        self.Number = tk.Label(self, text='背號：').grid(row=2, column=0, sticky='w')
        self.B_t = tk.Label(self, text='投打習慣：').grid(row=3, column=0, sticky='w')
        self.Ht_wt = tk.Label(self, text='身高體重：').grid(row=4, column=0,sticky='w')
        self.Born = tk.Label(self, text='生日：').grid(row=5, column=0, sticky='w')

        TeamVar = tk.StringVar()
        TeamVar.set(Team)
        tk.Label(self,textvariable=TeamVar).grid(column=1,row=0)
            
        NameVar = tk.StringVar()
        NameVar.set(Name)
        tk.Label(self,textvariable=NameVar).grid(column=1,row=1)

        NumberVar = tk.StringVar()
        NumberVar.set(Number)
        tk.Label(self,textvariable=NumberVar).grid(column=1,row=2)

        B_tVar = tk.StringVar()
        B_tVar.set(B_t)
        tk.Label(self,textvariable=B_tVar).grid(column=1,row=3)

        Ht_wtVar = tk.StringVar()
        Ht_wtVar.set(Ht_wt)
        tk.Label(self,textvariable=Ht_wtVar).grid(column=1,row=4)

        BornVar = tk.StringVar()
        BornVar.set(Born)
        tk.Label(self,textvariable=BornVar).grid(column=1,row=5)

        print(f'跑到這{Born}')

