'''
cpbl
'''

import tkinter as tk
from tkinter import ttk
#from cpbl_treeview import cpblTreeView
from tkinter import messagebox
from tkinter.simpledialog import Dialog
from threading import Timer
import datasource
from PIL import Image

#自定義class 呼叫datasource讀取csv檔案跟匯入資料庫的function
class Window(tk.Tk, ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except Exception: 
            messagebox.showerror('錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy()
#-------------------------------建立介面--------------------------------------------
#------------------------------最上面的標題---------------------------------------
        topFrame =tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        #只要裡面有內容，topFrame的邊框&預設大小就會失效，除非下Label的邊框距離設定
        #建立Label標籤放在topFrame裡面，設定與邊框的距離
        tk.Label(topFrame,text='中華職棒球員資料查詢',font=('arial,40'),bg='#333333',fg='#FFFFFF',pady=20).pack(fill='both', pady=20, padx=20)  
        topFrame.pack(pady=30)

#-----------------------------查詢介面-----------------------------------
        #建立容器元素
        middleFrame = ttk.LabelFrame(self,text='',relief=tk.GROOVE,borderwidth=1)
        
        #建立標籤
        tk.Label(middleFrame,text='球員搜尋').pack(side='left')

        #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.on_key_release)
        search_entry.pack(side='left')     
        middleFrame.pack(fill='x',padx=20)

#------------------------------球員個人資料、PR數據---------------------------------------
        infoFrame = ttk.LabelFrame(self,text='球員資料',relief=tk.GROOVE,borderwidth=1)
        infoFrame.pack()

        data = [2022, '富邦', 368, '游霆崴', 12, 4, 8, 1, 1, 0, 0, '30.1', 125, 27, 3, 11, 22, 10, '右投右打', 80, '178(CM) / 68(KG)', '1997/10/11', 'https://www.cpbl.com.tw/files/atts/0L087781916872199278/80游霆崴.jpg']

        self.Team = data[1]
        self.Name = data[3]
        self.B_t = data[18]                 
        self.Number = data[19]
        self.Ht_wt = data[20]
        self.Born = data[21]

        tk.Label(infoFrame, text='所屬球隊：').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        tk.Label(infoFrame, text='球員姓名：').grid(row=1, column=0, sticky='w',  padx=5, pady=5)
        tk.Label(infoFrame, text='背號：').grid(row=2, column=0, sticky='w',  padx=5, pady=5)
        tk.Label(infoFrame, text='投打習慣：').grid(row=3, column=0, sticky='w',  padx=5, pady=5)
        tk.Label(infoFrame, text='身高體重：').grid(row=4, column=0,sticky='w',  padx=5, pady=5)
        tk.Label(infoFrame, text='生日：').grid(row=5, column=0, sticky='w',  padx=5, pady=5)

        TeamVar = tk.StringVar()
        TeamVar.set(self.Team)
        tk.Label(infoFrame,textvariable=TeamVar, state='disabled').grid(row=0, column=1,  padx=5, pady=5)
            
        NameVar = tk.StringVar()
        NameVar.set(self.Name)
        tk.Label(infoFrame,textvariable=NameVar, state='disabled').grid(row=1, column=1,  padx=5, pady=5)

        NumberVar = tk.StringVar()
        NumberVar.set(self.Number)
        tk.Label(infoFrame,textvariable=NumberVar, state='disabled').grid(row=2, column=1,  padx=5, pady=5)

        B_tVar = tk.StringVar()
        B_tVar.set(self.B_t)
        tk.Label(infoFrame,textvariable=B_tVar, state='disabled').grid(row=3, column=1,  padx=5, pady=5)

        Ht_wtVar = tk.StringVar()
        Ht_wtVar.set(self.Ht_wt)
        tk.Label(infoFrame,textvariable=Ht_wtVar, state='disabled').grid(row=4, column=1,  padx=5, pady=5)

        BornVar = tk.StringVar()
        BornVar.set(self.Born)
        tk.Label(infoFrame,textvariable=BornVar, state='disabled').grid(row=5, column=1,  padx=5, pady=5)

        print(f'跑到這{self.Born}')
        
        

##-----------------------------建立隊伍按鈕-----------------------------------

        middle1Frame = ttk.LabelFrame(self,text='選擇球隊',relief=tk.GROOVE,borderwidth=1)
        tk.Label(middle1Frame,text='選擇球隊').pack
        middle1Frame.pack(fill='x', padx=20, pady=20)

        def team_search(event:None, word:str):
            print(word)
            rows = datasource.search_by_team(event=None, word=word)
            self.update_content(site_datas=rows)

        tk.Button(middle1Frame, text='中信兄弟', command=lambda: team_search(event=None,word='中信')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='樂天桃猿',command=lambda: team_search(event=None,word='樂天')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='統一7-ELEVEn獅',command=lambda: team_search(event=None,word='統一')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='富邦悍將',command=lambda: team_search(event=None,word='富邦')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        tk.Button(middle1Frame, text='味全龍',command=lambda: team_search(event=None,word='味全')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        

#------------------------------建立treeView-----------------------------------------
        self.TreeView=self.cpblTreeView(parent)
        self.TreeView['columns'] = ('Year', 'Team Name', 'ID', 'Name', 'G', 'GS', 'GR', 'W', 'L', 'SV', 'HLD', 'IP', 'BF', 'H', 'HR', 'BB', 'SO', 'ER')
        self.TreeView.pack(side='left')
    
    
    def cpblTreeView(self,parent,**kwargs):
        #super().__init__(parent,**kwargs)
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
        
        bottomFrame = tk.Frame(self)
        

        #設定捲動軸 
        
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.TreeView.yview)
        vsb.pack(side='left',fill='y')
        self.TreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20) #pady=(與上段距離，與下段距離)
        
        #--------------bind button1-------------------------
        self.bind('<ButtonRelease-1>',self.selectionItem)

        #-------------更新資料內容------------------------
        def update_content(site_datas):
                #必須先清除所有內容
                for i in self.TreeView.get_children():
                    self.TreeView.delete(i)
                
                for index, site in enumerate(site_datas):
                     self.TreeView.insert('', 'end', text=f'abc{index}', values=site)
        
        self.update_content = update_content

        #點擊treeView時，啟動此方法，回傳使用者點擊資料
    def selectionItem(self, event)->list:
            print(f'全域變數到selectionItem{t}')
            selectedItem = self.focus()
            data_dict = self.item(selectedItem)
            t = data_dict['values']
            print(f'selectionItem查詢結果{t}')

            #將資料傳入彈出視窗
            title_name = t[0]
            detail = ShowDetail(self.parent, data=t, title=title_name)
            #self.frame(t)
            

#-----------------------------更新treeView資料--------------------------------------
            lastest_data = datasource.lastest_datetime_data()               
            self.update_content(lastest_data)

#-----------------------------接收輸入的資料，並查詢&更新TreeView--------------------------------------
    def on_key_release(self, event):
        search_entry = event.widget  
        #print(search_entry)    
        #使用者輸入的文字  
        input_word = search_entry.get()
        print(input_word)
        
        if input_word == '':                                          #如果是空的，就自動更新最新資料在TreeView
            lastest_data = datasource.lastest_datetime_data()
            self.update_content(lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_word)  #如果有輸入值，就把輸入的值傳回search_sitename中查詢，並傳回結果&更新TreeView 
            self.update_content(search_data)      
    
#-----------------------------主程式定期自動更新資料--------------------------------------
def main():     
    def update_data(w:Window)->None:   
        datasource.update_sqlite_data()
        #-----------------------------更新treeView資料--------------------------------------
        latest_data = datasource.lastest_datetime_data()    #呼叫資料接收
        w.update_content(latest_data)
        print('資訊更新')

    window = Window(Window) 
    window.title('中華職棒球員資料查詢')
    window.resizable(width=True,height=True) 
    update_data(window)
    window.mainloop() 


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


if __name__ == '__main__':
    main()
