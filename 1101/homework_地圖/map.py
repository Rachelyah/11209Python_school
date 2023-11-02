'''
必須先安裝 tkintermapview套件（pip install tkintermapview）
'''

import tkinter as tk
import tkintermapview as tkmap


#-------------------------建立預設柏林地址的地圖---------------------------

class Window(tk.Tk):
   def __init__(self):
       super().__init__()
       #建立地圖
       map_widget = tkmap.TkinterMapView(self,
                                         width=800,
                                         height=600,
                                         corner_radius=0
                                         )
       map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
   window = Window()
   window.geometry("800x600")
   window.title("地圖")
   window.mainloop()