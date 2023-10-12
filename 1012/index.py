import tkinter as tk 
#為避免命名衝突，我呼叫tkinter這個資料夾並幫他取小名為tk

def main():
    window = tk.Tk() #建立一個叫做windows的視窗
    window.title("這是第一個視窗") #幫我的視窗設定一個名字
    label = tk.Label(window, text = "Hello!", font=('Helvetica', '30')) #設定一個label的原件，使用tk.Label方法放入內容並做設定
    label.pack(padx=100, pady=50) 


    window.mainloop() #讓視窗在主程式一直執行不要結束等待下一個指令，直到使用者關閉視窗才會停止運作，這一定會寫在最後面


if __name__ == "__main__":
    main()                  