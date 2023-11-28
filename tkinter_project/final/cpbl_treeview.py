import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
from PIL import Image, ImageTk
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import fontManager


t = [2022, '楊志龍','ACN','中信',40,0,40,0,0,0,2,4,0,12,37.0,158,628,31,0,16,0,4,42,4,0,20,17,34,31,2022,'右投右打',56,'189(CM) / 102(KG)'
     ,'1993/04/07','https://www.cpbl.com.tw/files/atts/0L087782012129886612/56楊志龍.jpg',10.22,4.14]

class cpblTreeView(ttk.Treeview):

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
        self.column('Year',width=70,anchor='center') 
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
    

       #將資料傳入彈出視窗
       title_name = t[3]
       print(f'球員姓名{title_name}')
       #detail = ShowDetail(self.parent, data=t, title=title_name)
       
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


class player():
    
    @staticmethod
    def player_name():
        player_name_list = t[3]
        return player_name_list
    
    @staticmethod
    def list_info():
        global t
        print(f'list_info{t}')
        player_info = t
        return player_info
    
    @staticmethod
    def k9_era():
        # 與原本的 calculate_k9, calculate_era 方法一起移到這裡
        def calculate_k9(so, ip):
            try:
                k9 = (so / ip) * 9
                return round(k9, 2)
            except ZeroDivisionError:
                return 0.0

        def calculate_era(er, ip):
            try:
                era = (er * 9) / ip
                return round(era, 2)
            except ZeroDivisionError:
                return 0.0

        # 原有的csv檔案
        cpbl_pitchings_csv = 'pitchings_2022_updated.csv'

        # 初始化變數以保存平均值
        total_k9 = 0.0
        total_era = 0.0
        count = 0

        with open(cpbl_pitchings_csv, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                so = float(row['SO'])
                ip = float(row['IP'])
                er = float(row['ER'])

                k9 = calculate_k9(so, ip)
                era = calculate_era(er, ip)

                total_k9 += k9
                total_era += era
                count += 1

        # 計算平均值
        average_k9 = round((total_k9 / count if count > 0 else 0.0), 2)
        average_era = round((total_era / count if count > 0 else 0.0), 2)

        print(f'平均 K9: {average_k9}')
        print(f'平均 ERA: {average_era}')

        return average_k9, average_era

    
    @staticmethod
    def pr_value(container):
        global t
        data = t

        if len(data) >= 20:
            k9_value = data[23]
            era_value = data[24]

            try:
                k9_values = float(k9_value)
                era_values = float(era_value)
            except ValueError:
                print("無法將 K9 或 ERA 值轉換為浮點數。")
                return

            # 在此設定中文字型的路徑
            #font_path = '/Users/rachelyeh/Documents/Python應用實戰/課程資料/徐國堂/GitHub/11209Python_school/tkinter_project/testphoto/NotoSansTC-VariableFont_wght.ttf'  # 請替換成實際的字型檔案路徑

            # 設定中文字型
            #font_prop = FontProperties(fname=font_path)
            #sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

            # 設定 Seaborn 樣式
            #sns.set(style="darkgrid", rc={"axes.facecolor": "#363636", "grid.color": "#363636", "text.color": "#363636"})
            
            # 設定 Matplotlib 樣式
            plt.style.use('dark_background')

            fig, ax = plt.subplots(figsize=(1.3, 1.3))
            #ax.set_yticks([])

            # 繪製長條圖
            sns.barplot(x=['K9', 'ERA'], y=[k9_values, era_values], errorbar=None, ax=ax, color='#0F4C3A',width=0.5)
            sns.despine(top = True, right = True, left=True, bottom=True) # 移除上方跟右方的框線
            
            # 在每一根長條上顯示 y 值
            for i, value in enumerate([k9_values, era_values]):
                ax.text(i, value, f'{value:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=5, color='white')
            #fontproperties=font_prop
            # 叫出平均值
            average_k9, average_era = player.k9_era()

            # 加入平均線
            ax.axhline(average_k9, color='#66BAB7', linestyle='dashed', linewidth=1, label='Average K9')
            ax.axhline(average_era, color='#B1B479', linestyle='dashed', linewidth=1, label='Average ERA')

            # 設定 legend 的位置，將 bbox_to_anchor 設置為 (1.05, 1)
            #ax.legend(bbox_to_anchor=(7, 0.1))
            #ax.legend(bbox_to_anchor=(-1.1, 1), loc='upper left', borderaxespad=2)

            #legend = ax.legend(['Average K9', 'Average ERA'], bbox_to_anchor=(7, 0.1), fontsize=5, title_fontsize=5)
            plt.legend(labels=["average_k9", "average_era"], loc='lower left',fontsize=5)
            
            # 設定標題
            #ax.set_title('K9 & ERA')
            #ax.legend()

            # 調整 x 和 y 軸上的標籤大小
            ax.tick_params(axis='x', labelsize=5)
            ax.tick_params(axis='y', labelsize=5)

            # 创建 FigureCanvasTkAgg 对象
            canvas = FigureCanvasTkAgg(fig, master=container)
            canvas.draw()

            # 获取 tkinter 的绘制区域并打包到容器中
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side='left', fill='both', expand=True)

            return canvas
        else:
            print("data 中的元素數量不足，無法取得 K9 與 ERA 數據。")