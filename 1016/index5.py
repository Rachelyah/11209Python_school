#Treeview樹狀選單

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        #self.geometry("300x250")
        #self.configure(background='#E79460')

class GetPassword(Dialog):

    def body(self, master):
        self.title("Enter New Password")

        tk.Label(master, text='Old Password:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='New Password:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='Enter New Password Again:').grid(row=2, sticky=tk.W)

        self.oldpw = tk.Entry(master, width=16, show='*')
        self.newpw1 = tk.Entry(master, width=16, show='*')
        self.newpw2 = tk.Entry(master, width=16, show='*')

        self.oldpw.grid(row=0, column=1, sticky=tk.W)
        self.newpw1.grid(row=1, column=1, sticky=tk.W)
        self.newpw2.grid(row=2, column=1, sticky=tk.W)
        return self.oldpw
    
    def buttonbox(self):
        '''add standard button box.
        override if you do not want the standard buttons
        '''
        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)
        
        #建立三個欄位，show='headings' 顯示最上面
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3'],show="headings")
        self.tree.heading('#1', text="第一欄")
        self.tree.heading('#2', text="第二欄")
        self.tree.heading('#3', text="第三欄")

        contacts = [] #建立一個空的list
        for n in range(1,100): #在n裡面依照順序放入1~100的數列
            contacts.append([f'first {n}',f'last {n}',f'email{n}:example.com']) 
           #把n的資料分成三組資料存入list，每一筆資料會長這樣 ['first 22', 'last 22', 'email22:example.com']
           #會自動執行99次，建立99個list

        for contact in contacts: 
            self.tree.insert('m',tk.END,value=contact)
            #再每一筆資料的結尾新增空字串(空一行)
            print(contact)
        
        self.tree.pack() #反正一定要寫pack才會把內容顯示出來

        #註冊在self.tree中，當點擊發生時要有下一步(函數方法叫做item.selected)
        self.tree.bind('<<TreeviewSelect>>',self.item_selected) 
    
    #當我的self.tree被點擊時，觸發這個方法
    def item_selected(self,event): #一定要有一個參數，不一定是event
        item_id = self.tree.selection()[0] #設定一個item_id，獲取使用者選擇的行&列 
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])
        dialog = GetPassword(self)

def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()

if __name__ == "__main__":
    main()