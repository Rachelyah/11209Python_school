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

class GetPassword(Dialog): #繼承Dialog
    
    #重設密碼的自定義方法（現成ㄉ）
    def body(self, master): #一個叫做body的方法，這裡規定只能被叫body，不能取別的名字
        self.title("Enter New Password")

        tk.Label(master, text='Old Password:').grid(row=0, sticky=tk.W) #sticky=tk.W（向左對齊）
        tk.Label(master, text='New Password:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='Enter New Password Again:').grid(row=2, sticky=tk.W)

        self.oldpw = tk.Entry(master, width=16, show='*')
        self.newpw1 = tk.Entry(master, width=16, show='*')
        self.newpw2 = tk.Entry(master, width=16, show='*')

        self.oldpw.grid(row=0, column=1, sticky=tk.W)
        self.newpw1.grid(row=1, column=1, sticky=tk.W)
        self.newpw2.grid(row=2, column=1, sticky=tk.W)
        return self.oldpw #這邊傳回舊密碼通常是先確認舊密碼是否正確，再寫入新的密碼
    
    def buttonbox(self): #複寫Dialog說明文件內的程式碼，需要完整複製過來後改（Dialog>查看定義）
        '''add standard button box.
        override if you do not want the standard buttons
        '''
        box = tk.Frame(self) #建立一個容器box

        #button = ttk.Button(container, text, command)
        #container＝你的按鈕要放在哪裡？>放在box
        #command=針對按鈕被點擊時觸發的下一步
        #當選擇確認時，觸發self.ok，並且確認鍵為預設選擇，使用者可以用Enter直接確認
        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        #當選擇到取消時，觸發self.cancel
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok) #綁定了對確認事件的操作，點擊確認>觸發self.ok
        self.bind("<Escape>", self.cancel) #同上

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
            self.tree.insert('',tk.END,value=contact)
            #再每一筆資料的結尾新增空字串(空一行)
        
        self.tree.pack() #反正一定要寫pack才會把內容顯示出來

        #註冊在self.tree中，當點擊發生時要有下一步(函數方法叫做item.selected)
        self.tree.bind('<<TreeviewSelect>>',self.item_selected) 
    
    #當我的self.tree被點擊時，觸發這個方法
    def item_selected(self,event): #一定要有一個參數，不一定要寫event
        #設定一個item_id，獲取使用者選擇的行&列
        #傳回使用者點選的list[0]，通常就是第一欄位的內容
        item_id = self.tree.selection()[0] 
        self.tree.item(item_id)
        #.item()會傳回dict{}，包含text, image, values等
        item_dict = self.tree.item(item_id)
        #抓出dict{}裡的values
        print(item_dict['values'])
        #呼叫GetPassword類別
        dialog = GetPassword(self)

def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()

if __name__ == "__main__":
    main()