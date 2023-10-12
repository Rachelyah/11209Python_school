#嘗試用物件導向&繼承寫法改寫index.py

import tkinter as tk 
from tkinter import ttk 
#打開ttk資料夾(差別在於Label的用法，目前下面是舊的用法)
#如果要用新的，可以寫label = ttk.Label()

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("這是第一個視窗")
        label = tk.Label(self, text = "Hello!", font=('Helvetica', '30')) 
        label.pack(padx=100, pady=50) 

def main():
    window = Window() 
    window.mainloop()

if __name__ == "__main__":
    main()                  