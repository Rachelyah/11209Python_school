import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#E79460')

class MyFrame(ttk.LabelFrame): #跟tk的Frame不一樣，多可以用text寫說明的功能
    def __init__(self,master, title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        #self.configure(background='#9E7A7A')
        #ttk不能用背景色，ttk類似css的用法
        self.aligement = tk.StringVar(value='center') #設定預設值是中間(一開始選項會自動選擇中間)
        ttk.Radiobutton(self, text="左邊", variable=self.aligement, command=self.choised, value='left').grid(column=0,row=0, padx=10) #要寫variable這個變數，儲存預設值，並寫在rariobutton中連結(每個選項都要寫)
        ttk.Radiobutton(self, text="中間", variable=self.aligement, command=self.choised, value='center').grid(column=1,row=0, padx=10)
        ttk.Radiobutton(self, text="右邊", variable=self.aligement, command=self.choised, value='right').grid(column=2,row=0, padx=10) 
        self.pack(expand=1, fill='both', padx=10, pady=10)
        print(self.winfo_class()) #TLabelframe 目前樣式的標籤名稱，css選取器可以標設定的名稱
        self.style = ttk.Style(self) #我設定一個self.style套用ttk.Style()
        #self.style.configure('First.TLabel')
        self.style.configure('TLabelframe.Label', font=('Helvetica', 20),foreground='red',background='black')
        #confugure或是config都可以， 針對TLabelframe做樣式設定(為甚麼只有對齊方式被改？)

    #自動print出使用者選擇的value
    def choised(self): #不需要給參數，bind才必要
        print(self.aligement.get())

def main():    
    window = Window()
    myFrame = MyFrame(window, "對齊方式")
    #s = ttk.Style() #會傳出有哪些theme，會傳出turple
    #print(s.theme_names()) #查詢有哪些樣式？
    #print(s.theme_use())   #我現在用的樣式？
    #s.theme_use('default')    #我想要改為''樣式
    window.mainloop()

if __name__ == "__main__":
    main()