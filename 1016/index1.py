#使用Pillow套件繪製圖像
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk 

class Window(tk.Tk):
    def __init__(self, **kwargs):     
        super().__init__(**kwargs)
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#255359') 
        

class MyFrame(tk.Frame):
    def __init__(self, master, **kwargs): 
        super().__init__(master, **kwargs) 
        self.configure(background='#86A697')
        self.img = Image.open("people.png")
        self.people = ImageTk.PhotoImage(self.img)
        canvas = tk.Canvas(self, 
                           width=48,
                           height = 48)
        canvas.create_image(24,24 ,image=self.people,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1, fill='both') 

def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()
