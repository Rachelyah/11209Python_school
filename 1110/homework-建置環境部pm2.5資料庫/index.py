import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pm25_treeview import pm25_treeview
from threading import Timer
import datasource
import psycopg2
import password as pw

#-------------建立視窗----------------
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        #---------建立介面------------------------
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="全台pm2.5即時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)

    #----------建立搜尋------------------------
        middleFrame = ttk.LabelFrame(self,text='')
        tk.Label(middleFrame,text='測站名稱搜尋:').pack(side='left')
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.OnEntryClick)
        search_entry.pack(side='left')        
        middleFrame.pack(fill='x',padx=20)

    #---------------建立treeView---------------
        bottomFrame = tk.Frame(self)
        self.pm25_treeview = pm25_treeview(bottomFrame,
                                           columns=('site','county','pm25','datacreationdate'),
                                           show="headings",
                                           height=20)
        self.pm25_treeview.pack(side='left')
        #設置滾動軸
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.pm25_treeview.yview)
        vsb.pack(side='left',fill='y')
        self.pm25_treeview.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30),padx=20)

    #回傳使用者輸入的內容
    def OnEntryClick(self,event):
            searchEntry = event.widget
            #使用者輸入的文字
            input_word = searchEntry.get()
            if input_word == "":
                lastest_data = datasource.lastest_datetime_data()
                self.pm25_treeview.update_content(lastest_data)
            else:
                search_data = datasource.search_sitename(word=input_word)
                self.pm25_treeview.update_content(site_datas=search_data)


def main():
    def update_data(w:Window)->None:
        #-----------更新treeView資料---------------   
        try:
            datasource.updata_render_data()

        except Exception as e:
            print(f"錯誤,網路不正常\n{e}")
            messagebox.showerror(f"錯誤,網路不正常\n{e}\n將關閉應用程式\n請稍後再試")

        lastest_data = datasource.lastest_datetime_data()
        w.pm25_treeview.update_content(lastest_data)
        
        #w.after(5*60*1000,update_data,w) #每隔5分鐘
        t = Timer(5*60, update_data,args=(window,))
        t.start()

    window = Window()
    window.title('全台pm2.5即時資料')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    lastest_data = datasource.lastest_datetime_data()
    window.pm25_treeview.update_content(lastest_data)
    #window.after(1000,update_data,window) 
    t = Timer(1, update_data,args=(window,))
    t.start()         
    window.mainloop()
    

    

if __name__ == "__main__":
    main()