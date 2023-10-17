# 用物件導向&繼承寫法改寫index.py

import dataSource
import tkinter as tk 
from tkinter import ttk

# 打開ttk資料夾(差別在於Label的用法
# 如果要用新的，可以寫label = ttk.Label()

# 設定listbox
# listbox = tk.Listbox(container, listvariable, height)
# 自定一個叫做Windows的class，並且繼承Tk這個包裹裡面所有的Class設定（tk是我們自己取的）

class Window(tk.Tk):
    #建立一個視窗(*父容器)，預設底色與title
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("鄉鎮人口統計")
        self.configure(background='#268785') #視窗底色預設沒有大小

    #我在裡面放一個容器，取名為topFrame
    #topFrame裡面放Label標籤，放入文字跟padding設計
    #要排版呈現在畫面中，一定要用pack()或是預設layout
    #tkinter預設有三種layout方式(pack上下左右/grid表格/Place)
    #當你用了pack()整個視窗就都只能用pack()
        topFrame = tk.Frame(self, background='#261E47')
        label = ttk.Label(topFrame, text = "鄉鎮人口統計", font=('Helvetica', '30')) 
        label.pack(padx=20, pady=20) 
        topFrame.pack()

    #選單
    #下面再放一個容器bottomFrame，程式由上讀到下，會自動放在topFrame下面
    #放入listbox
    #listbox = tk.Listbox(container, listvariable, height)
    #tk.StringVar 儲存動態文字用(按鈕跟list的設定會用到)

        bottomFrame = tk.Frame(self, background='#4E4F97')
        choices = dataSource.cityNames()    #建立choices放cityNames的資料
        choicevar = tk.StringVar(value=choices) #再建立一個choicevar把動態文字存入
        self.listbox = tk.Listbox(bottomFrame, listvariable=choicevar, width=13)
        self.listbox.pack(pady=20)
        bottomFrame.pack(expand=True, fill='x')
        
        #box.bind 當使用者選取listbox中的內容時，跑出一個print('user selected')
        #需要搭配def使用，當有使用者點選選單時，觸發這個def
        self.listbox.bind("<<ListboxSelect>>", self.user_selected)

        #現在我想要建立表格呈現我的資料結果
        #layout建議用grid()，但我上面都已經用pack()了，不能換
        #所以我建立新的容器，在裡面用gird()，再用pack()呈現實體
        #把表格的文字靠右 sticky='w'(東西南北)
        
        resultFrame = tk.Frame(self)
        tk.Label(resultFrame, text='年度:').grid(column=0, row=0, sticky='w', pady=5)
        tk.Label(resultFrame, text='地區:').grid(column=0, row=1, sticky='w', pady=5)
        tk.Label(resultFrame, text='人口數:').grid(column=0, row=2, sticky='w', pady=5)
        tk.Label(resultFrame, text='土地面積:').grid(column=0, row=3, sticky='w', pady=5)
        tk.Label(resultFrame, text='人口密度:').grid(column=0, row=4, sticky='w', pady=5)
        
        #把所有查詢的資料變成變動資料存入變數
        #再透過
        self.yeatVar = tk.StringVar()
        tk.Label(resultFrame, textvariable=self.yeatVar).grid(column=1, row=0, sticky='w', pady=5)
        
        self.cityVar = tk.StringVar()
        tk.Label(resultFrame, textvariable=self.cityVar).grid(column=1, row=1, sticky='w', pady=5)

        self.populationVar = tk.StringVar()
        tk.Label(resultFrame, textvariable=self.populationVar).grid(column=1, row=2, sticky='w', pady=5)

        self.areaVar = tk.StringVar()
        tk.Label(resultFrame, textvariable=self.areaVar).grid(column=1, row=3, sticky='w', pady=5)

        self.densityVar = tk.StringVar()
        tk.Label(resultFrame, textvariable=self.densityVar).grid(column=1, row=4, sticky='w', pady=5)  

        resultFrame.pack()

    #這個method裡面需要一個參數來接受，不一定要是event，叫甚麼都可以
    #通常我的listbox，只能在一個class的__init__裡面用
    #但我想要跳出上面的def後也可以被外面的def讀到，所以我在上面的user_selected(註冊)的地方寫入self.user_selected，這樣就等同於我的listbox也被註冊了，只要是self.listbox就可以被外面的def讀取

    #使用listbox = tk.Listbox(container, listvariable, height)
    #Listbox.curselection() 取得目前 Listbox 的選項
    def user_selected(self, event):
        
        selectedIndex = self.listbox.curselection()[0]
        print(selectedIndex)#＞會得到turple
        #[0]的意思代表listbox裡面的資料＞choicevar(來源是dataSource.cityNames()的結果)，
        #我再利用list.get把我要的資料抓出來
        cityName = self.listbox.get(selectedIndex)
        print(dataSource.info(cityName))
        #拿著序號回去查datasource裡面的資料：第幾筆資料內容是甚麼區？再傳回datalist
        datalist = dataSource.info(cityName)
        self.yeatVar.set(datalist[0]) #把datalist查出特定欄位的值，傳到我指定的變數裡面
        self.cityVar.set(datalist[1])
        self.populationVar.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])

def main():
    window = Window() 
    window.mainloop()

if __name__ == "__main__":
    main()                  