#Python檔案內建的名稱，只有他被當作執行檔時才會執行內容

'''
學習Canvas
'''
import tkinter as tk #舊版
from tkinter import ttk #新的package叫做ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):     #override
        super().__init__(**kwargs)
        self.geometry("400x300+300+300") 
    #設定視窗大小，用字串呈現(geometry='120x50-0+20' *視窗開啟時往右多少座標、往下多少座標)
        self.title("Lines")
        self.configure(background='#255359') 

class MyFrame(tk.Frame):
    def __init__(self, master, **kwargs): 
        #預設master:MISC|None ->代表這個容器要放到哪個父容器裡面(預設值是None，改寫預設值，我要放到Window這個視窗裡面) / **->引述名稱+引數值
        super().__init__(master, **kwargs) #改寫master的預設為必須輸入的參數
        self.configure(background='#86A697') #Frame本來預設沒有大小，當沒有放內容就看不到
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200, 30) 
        canvas.create_line(300, 35, 300, 200, dash=(4,2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(expand=1, fill='both')
        self.pack(expand=1, fill='both') #expand擴充(0&1 or True&False) #fill填滿(x左右、y上下、both全部)


def main():
    '''
    使用說明書
    param:如果有參數，會在這邊說明參數內容
    
    '''
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()
