#要執行的檔案會寫if __name__ == "__main__"
#我的下載def寫在dataSource這個module裡面
#目前都沒有把檔案建立及寫入在本地端，每次執行我都是透過download()去網路上下載一次資料，酷喔

import dataSource  

def main():
    cities = dataSource.cities_info()  #我建立一個cities_data的變數，透過dataSource.cities_info()這個method去運作，回傳值放到cities(也可以是其他變數名)
    for city in cities: #透過for in迴圈列出我要蒐集的資料，會比較好看
        print(city)

    names = dataSource.cityNames() #建立names變數接收這個方法的回傳結果(str)
    city = dataSource.info(name = '基隆市仁愛區') #建立city，並輸入我要查詢的name='地區，會跑出我要查詢的結果
    print(names)
    print(city)

if __name__ == "__main__":
    main()                  #很多應用程式的執行點都在main()