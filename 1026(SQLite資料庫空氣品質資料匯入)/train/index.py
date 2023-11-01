import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs) 
        
        #視窗設定
        self.configure(background='#268785')
        topFrame = tk.Frame(self, background='#261E47')
        label = ttk.Label(topFrame, text = "台北市立圖書館剩餘座位", font=('Helvetica', '30')) 
        label.pack(padx=20, pady=20) 
        topFrame.pack()
        
        #下載圖書館即時剩餘座位資料
        try:
            datasource.update_sqlite_data()
        except Exception as e: 
            messagebox.showerror(f'下載錯誤 {e}') 
            self.destroy()

#建立容器Frame，裡面放樹狀選單＋匯入CSV資料＋滾動軸
class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)
        #建立treeView欄位
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="Adj Close")
        self.tree.heading('#7', text="Volume")

t=None 
def main():
    def on_closing():            
        print('window關閉')
        t.cancel()               
        window.destroy()            

    def update_data()->None:
        datasource.update_sqlite_data()
        print('資訊更新')
        global t                   
        t = Timer(20, update_data) 
        t.start()                 

    window = Window()             
    window.title('台北市圖書館即時座位查詢')   
    window.geometry('600x300')        
    window.resizable(width=False ,height=False) 
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()            


if __name__ == '__main__':
    main()