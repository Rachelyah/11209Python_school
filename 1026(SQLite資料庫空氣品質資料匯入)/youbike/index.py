'''
下載台北市youbike2.0的資料
'''

#將tkinter的包裹取名為tk
#tkinter裡面有很多package裡面有class
#tkinter裡面有一個class叫TK，包含所有視窗的功能

import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義class的屬性
        super().__init__(**kwargs) #繼承原本Tk的屬性(self不用寫)
        try:
            datasource.update_sqlite_data()
        except Exception: #當datasource傳出Exception
                          #套用messangebox.showerror方法，跳出另一個視窗呈現錯誤訊息
            messagebox.showerror('下載錯誤', '網路不正常\n將關閉應用程式\n請稍後再試') 
            self.destroy() #自動關閉視窗

t=None  #先建立一個全域變數定義t
def main():
    def on_closing():               #括號內的w:Window可以省略，因為跟window在同一個function裡
        print('window關閉')
        t.cancel()                  #執行緒中斷(取消Timer)
        window.destroy()            #關閉視窗

#更新資料的function
    def update_data()->None:
        datasource.update_sqlite_data()
        print('資訊更新')
        global t                    #表示我呼叫的是全域(文件)變數的t，不是單純這個function的t
        t = Timer(20, update_data)  #每20秒呼叫一次function
        t.start()                   #開始執行這個thread

    window = Window()               #建立一個window執行Window()
    window.title('台北市youbike2.0')    #設定視窗的title
    window.geometry('600x300')          #設定視窗大小
    window.resizable(width=False ,height=False) #固定視窗大小
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    # window.protocol("WM_DELETE_WINDOW",lambda : on_closing(window)) 
    # 一個註冊的寫法
    # 沒有傳遞東西過去就不用寫lambda 不同def之間互傳才要寫上面這樣，但上面的def全部包在main裡
    # lambda 匿名的function，請執行冒號後的動作，把這個function的window傳到on_closing裡
    window.mainloop()               #永遠執行視窗，直到使用者下一個動作

if __name__ == '__main__':
    main()