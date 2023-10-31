import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs) 
        self.configure(background='#268785')
        topFrame = tk.Frame(self, background='#261E47')
        label = ttk.Label(topFrame, text = "台北市立圖書館剩餘座位", font=('Helvetica', '30')) 
        label.pack(padx=20, pady=20) 
        topFrame.pack()
        try:
            datasource.update_sqlite_data()
        except Exception as e: 
            messagebox.showerror(f'下載錯誤 {e}') 
            self.destroy()
        
        bottomFrame = tk.Frame(self, background='#4E4F97')
        choices = datasource.update_sqlite_data() 
        choicevar = tk.StringVar(value=choices)
        self.listbox = tk.Listbox(bottomFrame, listvariable=choicevar, width=13)
        self.listbox.pack(pady=20)
        bottomFrame.pack(expand=True, fill='x')

        #self.listbox.bind("<<ListboxSelect>>", self.user_selected)

        resultFrame = tk.Frame(self)
        tk.Label(resultFrame, text='年度:').grid(column=0, row=0, sticky='w', pady=5)
        tk.Label(resultFrame, text='地區:').grid(column=0, row=1, sticky='w', pady=5)
        tk.Label(resultFrame, text='人口數:').grid(column=0, row=2, sticky='w', pady=5)
        tk.Label(resultFrame, text='土地面積:').grid(column=0, row=3, sticky='w', pady=5)
        tk.Label(resultFrame, text='人口密度:').grid(column=0, row=4, sticky='w', pady=5)



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