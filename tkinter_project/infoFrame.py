import tkinter as tk
from tkinter import ttk
from cpbl_treeview import cpblTreeView
from tkinter import messagebox
from threading import Timer
import datasource
from PIL import Image

import tkinter as tk

class InfoDisplay(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

#----------建立欄位---------------
    def create_widgets(self):
        tk.Label(self, text='球員姓名：').grid(row=0, column=0, sticky='w')
        tk.Label(self, text='背號：').grid(row=1, column=0, sticky='w')
        tk.Label(self, text='投打習慣：').grid(row=2, column=0, sticky='w')
        tk.Label(self, text='身高體重：').grid(row=3, column=0, sticky='w')
        tk.Label(self, text='生日：').grid(row=4, column=0, sticky='w')
        tk.Label(self, text='照片：').grid(row=5, column=0, sticky='w')

        tk.Label(self, text='').grid(row=0, column=1, sticky='w')
        tk.Label(self, text='').grid(row=1, column=1, sticky='w')
        tk.Label(self, text='').grid(row=2, column=1, sticky='w')
        tk.Label(self, text='').grid(row=3, column=1, sticky='w')
        tk.Label(self, text='').grid(row=4, column=1, sticky='w')
        tk.Label(self, text='').grid(row=5, column=1, sticky='w')