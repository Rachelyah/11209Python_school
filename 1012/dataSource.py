#把這個def設為不公開__download()
#我要擷取所有第0項的內容是'111'的資料，是我要的資料

import requests
import csv
import io

__cities = [] #這裡可以儲存變數，並且不可以讓外面的人看到

#下載原始資料的def
def __download() ->list[list] | Exception: 
    url='https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'

    response = requests.request('GET', url)

    try:
        response.raise_for_status()
    except:
        raise Exception('連線發生錯誤', '網路中斷')
    else:
        if not response.ok:
            raise Exception('下載錯誤', '伺服器錯誤訊息')
        else:
            file = io.StringIO(response.text) 
            csv_reader = csv.reader(file)     
            next(csv_reader) 
            return list(csv_reader) 

#將原始資料過濾&傳出的def       
def cities_info() -> list[list]: #二維list，這是提醒自己出來的值的型別，不寫也可以但建議要寫
    if len(__cities) == 0:    #用len計算字數，確定這個list裡面沒有東西，我才要開始下載
        try:
            data_list = __download()  #回去執行上面不公開的下載連結，並傳出值
        except Exception as e:      
            print(f'錯誤:{e}') 
        else:
            for row in data_list:     #用迴圈列出我要的資料
                if row[0] == '111':   
                    __cities.append(row) #用append將row中我要的資料寫入cities的最後面
    return __cities #蒐集完成後回傳值給index.py

#蒐集第2列的城市名稱
def cityNames() -> list[str]:  #建立一個cityNames的method，出來會是list
    cities = cities_info()     #建立cities變數，接取上面cities_info()出來的結果
    names=[]                   #建立空字串
    for row in cities:         #用for in迴圈，把cities的資料用row儲存
        cityName = row[1]      #在row中的第一列(城市)我用cityName定義，他會一直因為for迴圈更新
        names.append(cityName) #把cityName的資料寫入names這個空字串
    return names               #結果會得出一個list[str]

#老師滑鐵盧的def，可以多看幾次
#蒐集資料的list[str]，我輸入指定的第二列地區，查詢出相對應的結果
#建立一個引述名稱name並不給default，代表我一定要你輸入值才可以查
def info(name:str):
    cities = cities_info() 
    for city in cities:
        if city[1] == name:
            return city
    return []  #原本這邊有寫 else: return[]，但不管怎麼搜尋到跑到else這邊          

#矛盾的地方：因為他是for in迴圈會從第一個開始跑，所以如果我輸入搜尋的不是第一個的話，就會直接跑到else，所以我不能設定else的條件，除了第一個之外ㄑ
