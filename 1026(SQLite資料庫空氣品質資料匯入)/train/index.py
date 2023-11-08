import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs) 
        
        #---------下載圖書館即時剩餘座位資料--------------
        try:
            datasource.update_sqlite_data()
        except Exception as e: 
            messagebox.showerror(f'下載錯誤 {e}') 
            self.destroy()

        #----------建立介面----------------------------
        topFrame = tk.Frame(self, relief=tk.GROOVE,background='#261E47')
        tk.Label(topFrame, text = "台北市立圖書館剩餘座位", font=('Helvetica', '30')).pack(padx=20, pady=20)
        topFrame.pack()
        #bottomFrame = tk.Frame(self)
        
def main():       
    def update_data(w:Window)->None:
        datasource.update_sqlite_data()      
        window.after(1*10*1000,update_data, w)      
        print('資訊更新')                 

    window = Window()             
    window.title('台北市圖書館即時座位查詢')   
    window.geometry('600x300')        
    window.resizable(width=True ,height=True) 
    update_data(window)
    window.mainloop()            


if __name__ == '__main__':
    main()