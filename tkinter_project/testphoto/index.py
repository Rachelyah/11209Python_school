'''
cpbl
'''

import tkinter as tk
from tkinter import ttk
from cpbl_treeview import cpblTreeView
#from cpbl_treeview import Player_info
from cpbl_treeview import player
from tkinter import messagebox
from threading import Timer
import datasource
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import pandas

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        try:
            datasource.update_sqlite_data()
        except Exception: 
            messagebox.showerror('錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() 

#-------------------------------建立介面--------------------------------------------
#------------------------------最上面的標題---------------------------------------
        style = ttk.Style("cyborg")
        topFrame =tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text='中華職棒球員資料',font=('arial,40'),bg='#333333',fg='#FFFFFF',pady=20).pack(fill='both', pady=5, padx=5,ipadx=5,ipady=5,expand=True)
        topFrame.pack(pady=5,expand=True)
#----------------------------建立上層介面------------------------------------
        container = ttk.LabelFrame(self,text='球員資料',relief=tk.GROOVE,borderwidth=1)
        container.pack(fill='y', ipadx=5,ipady=5,padx=5,pady=5)
#-----------------------------建立查詢介面-----------------------------------
        #建立容器元素
        middleFrame = ttk.LabelFrame(self,text='球員搜尋',relief=tk.GROOVE,borderwidth=1)

        #建立輸入欄位
        search_entry = tk.Entry(middleFrame)
        search_entry.pack(side='top',ipadx=5,ipady=5,padx=5,pady=5, fill='y')     
        middleFrame.pack(side='top', ipadx=5,ipady=5,padx=5,pady=5, fill='y')
        search_entry.bind("<KeyPress>", self.on_key_release)
        #search_entry.bind("<FocusIn>", self.on_key_release)


#------------------------------球員個人資料、PR數據---------------------------------------
        
        photoFrame = ttk.LabelFrame(container,text='球員照片',relief=tk.GROOVE,borderwidth=1)
        photoFrame.pack(side='left', anchor="n", expand=True, ipadx=5,ipady=5,padx=5,pady=5, fill='y')
        self.tk_img = None

        self.infoFrame = ttk.LabelFrame(container, text='球員資料', relief=tk.GROOVE, borderwidth=1)
        self.infoFrame.pack(side='left', anchor="n", expand=True, ipadx=5,ipady=5,padx=5,pady=5)

        self.player_data = ttk.LabelFrame(container, text='奪三振率(K9值)&防禦率(ERA)', relief=tk.GROOVE, borderwidth=1)
        self.player_data.pack(side='left', anchor="n", ipadx=5,ipady=5,padx=5,pady=5, fill='y')

        prframe = ttk.LabelFrame(container, text='奪三振率(K9值)&防禦率(ERA)', relief=tk.GROOVE, borderwidth=1)
        prframe.pack(side='left', anchor="n", ipadx=5,ipady=5,padx=5,pady=5, fill='y')

        def info(event):  
            self.update_idletasks()

            for widget in self.infoFrame.winfo_children():
                widget.destroy()

            data = player.list_info()
            print(f'查看資訊{data}')
            Team_info = data[1]
            Name_info = data[3]
            B_t_info = data[18]                 
            Number_info = data[19]
            Ht_wt_info = data[20]
            Born_info = data[21]

            Team = tk.Label(self.infoFrame, text='所屬球隊：').grid(row=0, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            Name = tk.Label(self.infoFrame, text='球員姓名：').grid(row=1, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            Number = tk.Label(self.infoFrame, text='背號：').grid(row=2, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            B_t = tk.Label(self.infoFrame, text='投打習慣：').grid(row=3, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            Ht_wt = tk.Label(self.infoFrame, text='身高體重：').grid(row=4, column=0,sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            Born = tk.Label(self.infoFrame, text='生日：').grid(row=5, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)

            TeamVar = tk.StringVar()
            TeamVar.set(Team_info)
            print(f'Team{Team_info}')
            tk.Entry(self.infoFrame,textvariable=TeamVar,state='normal' ).grid(column=1,row=0)
                
            NameVar = tk.StringVar()
            NameVar.set(Name_info)
            tk.Entry(self.infoFrame,textvariable=NameVar,state='normal' ).grid(column=1,row=1)

            NumberVar = tk.StringVar()
            NumberVar.set(Number_info)
            tk.Entry(self.infoFrame,textvariable=NumberVar,state='normal' ).grid(column=1,row=2)

            B_tVar = tk.StringVar()
            B_tVar.set(B_t_info)
            tk.Entry(self.infoFrame,textvariable=B_tVar,state='normal' ).grid(column=1,row=3)

            Ht_wtVar = tk.StringVar()
            Ht_wtVar.set(Ht_wt_info)
            tk.Entry(self.infoFrame,textvariable=Ht_wtVar,state='normal' ).grid(column=1,row=4)

            BornVar = tk.StringVar()
            BornVar.set(Born_info)
            tk.Entry(self.infoFrame,textvariable=BornVar,state='normal' ).grid(column=1,row=5)
            
            #詳細資料
            for widget in self.player_data.winfo_children():
                widget.destroy()


            IP_info = data[15]
            SV_info = data[13]
            HLD_info = data[14]                 
            H_info = data[18]
            HR_info = data[19]
            BB_info = data[20]


            IP = tk.Label(self.player_data, text='有效局數：').grid(row=5, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            SV = tk.Label(self.player_data, text='救援成功：').grid(row=0, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            HLD = tk.Label(self.player_data, text='中繼成功：').grid(row=1, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            H = tk.Label(self.player_data, text='被安打數：').grid(row=2, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            HR = tk.Label(self.player_data, text='被全壘打數：').grid(row=3, column=0, sticky='w', ipadx=5,ipady=5,padx=5,pady=5)
            BB = tk.Label(self.player_data, text='保送數：').grid(row=4, column=0,sticky='w', ipadx=5,ipady=5,padx=5,pady=5)


            TeamVar = tk.StringVar()
            TeamVar.set(IP_info)
            print(f'Team{IP_info}')
            tk.Entry(self.player_data,textvariable=TeamVar,state='normal' ).grid(column=1,row=0)
                
            NameVar = tk.StringVar()
            NameVar.set(SV_info)
            tk.Entry(self.player_data,textvariable=NameVar,state='normal' ).grid(column=1,row=1)

            NumberVar = tk.StringVar()
            NumberVar.set(HLD_info)
            tk.Entry(self.player_data,textvariable=NumberVar,state='normal' ).grid(column=1,row=2)

            B_tVar = tk.StringVar()
            B_tVar.set(H_info)
            tk.Entry(self.player_data,textvariable=B_tVar,state='normal' ).grid(column=1,row=3)

            Ht_wtVar = tk.StringVar()
            Ht_wtVar.set(HR_info)
            tk.Entry(self.player_data,textvariable=Ht_wtVar,state='normal' ).grid(column=1,row=4)

            BornVar = tk.StringVar()
            BornVar.set(BB_info)
            tk.Entry(self.player_data,textvariable=BornVar,state='normal' ).grid(column=1,row=5)



            # 抓取球員照片
            for widget in photoFrame.winfo_children():
                if isinstance(widget, tk.Canvas):
                    widget.destroy()
            
            name = player.player_name()
            photo_path = f'./img/{name}.jpg'
            img = Image.open(photo_path)

            # 調整圖片大小為 120x160
            img = img.resize((120, 160), Image.BILINEAR)

            # 將圖片轉換為 Tkinter PhotoImage 對象，使用實例變數
            self.tk_img = ImageTk.PhotoImage(img)

            # 創建一個 Canvas 並在其中放入圖片
            canvas = tk.Canvas(photoFrame, width=120, height=160)
            canvas.pack(side='top', fill='both', expand=True)

            # 計算圖片在 Canvas 中的座標
            img_width, img_height = 120, 160
            x = (img_width - canvas.winfo_reqwidth()) / 2
            y = (img_height - canvas.winfo_reqheight()) / 2

            # 在 Canvas 中創建圖片
            canvas.create_image(x, y, anchor='nw', image=self.tk_img)

            for widget in prframe.winfo_children():
                widget.destroy()
            
            canvasphoto = player.pr_value(prframe)


##-----------------------------建立隊伍按鈕-----------------------------------

        middle1Frame = ttk.LabelFrame(self,text='選擇球隊',relief=tk.GROOVE,borderwidth=1)
        tk.Label(middle1Frame,text='選擇球隊').pack
        middle1Frame.pack(side='top',fill='x', ipadx=10,ipady=10,padx=10,pady=10, expand=True)

        def team_search(event:None, word:str):
            print(word)
            rows = datasource.search_by_team(event=None, word=word)
            self.cpblTreeView.update_content(site_datas=rows)
            self.bind('<ButtonRelease-1>',info)

        ttk.Button(middle1Frame, text='中信兄弟', style='info', command=lambda: team_search(event=None, word='中信')).pack(ipadx=25, ipady=10, side='left', expand='Yes')

        ttk.Button(middle1Frame, text='樂天桃猿',bootstyle='Danger',command=lambda: team_search(event=None,word='樂天')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        ttk.Button(middle1Frame, text='統一7-ELEVEn獅',bootstyle='Warning',command=lambda: team_search(event=None,word='統一')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        ttk.Button(middle1Frame, text='富邦悍將',command=lambda: team_search(event=None,word='富邦')).pack(ipadx=25, ipady=10, side='left', expand='Yes')
        ttk.Button(middle1Frame, text='味全龍',bootstyle='success',command=lambda: team_search(event=None,word='味全')).pack(ipadx=25, ipady=10, side='left', expand='Yes')


#------------------------------建立treeView-----------------------------------------
        bottomFrame = tk.Frame(self)
        self.cpblTreeView = cpblTreeView(bottomFrame,columns=('Year','Team Name','ID','Name','G', 'GS', 'GR', 'W', 'L', 'SV', 'HLD', 'IP', 'BF', 'H', 'HR', 'BB', 'SO', 'ER'),show="headings",height=20)
        #設定捲動軸 
        self.cpblTreeView.pack(side='left', fill='x', expand=True)
        vsb = ttk.Scrollbar(bottomFrame, orient='vertical',command=self.cpblTreeView.yview)
        vsb.pack(side='right',fill='y', expand=True)
        self.cpblTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30), padx=20) #pady=(與上段距離，與下段距離)  
#-----------------------------更新treeView資料--------------------------------------
        lastest_data = datasource.lastest_datetime_data()               
        self.cpblTreeView.update_content(site_datas=lastest_data)
        self.bind('<ButtonRelease-1>',info)

#-----------------------------接收輸入的資料，並查詢&更新TreeView--------------------------------------
        
    def on_key_release(self, event):
        search_entry = event.widget  
        #print(search_entry)    
        #使用者輸入的文字  
        input_word = search_entry.get()
        print(input_word)
        
        if input_word == '':                                          #如果是空的，就自動更新最新資料在TreeView
            lastest_data = datasource.lastest_datetime_data()
            self.cpblTreeView.update_content(lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_word)  #如果有輸入值，就把輸入的值傳回search_sitename中查詢，並傳回結果&更新TreeView 
            self.cpblTreeView.update_content(search_data)

'''
def on_search_entry_focus_in(self, event):
        # 解除 <KeyRelease> 事件和 <ButtonRelease-1> 事件的綁定
        self.search_entry.unbind("<ButtonRelease-1>")
        self.unbind('<ButtonRelease-1>')

        # 綁定 <KeyRelease> 事件到 on_key_release 方法
        self.search_entry.bind("<KeyRelease>", self.on_key_release)
'''
    
#-----------------------------主程式定期自動更新資料--------------------------------------
def main():     
    def update_data(w:Window)->None:   
        print('資訊更新')

    window = Window() 
    window.title('中華職棒球員資料查詢')
    window.resizable(width=True,height=True) 
    update_data(window)
    window.wait_window() 



if __name__ == '__main__':
    main()