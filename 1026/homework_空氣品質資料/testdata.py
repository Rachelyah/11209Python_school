'''
1. 建立moudle，下載環境部空氣品質資料的function
'''

import requests
import sqlite3
from datetime import datetime

# module裡面可以放function、變數、class
# function內要寫說明用多行文字
# import建議放在最上面，不然放在def裡面每進到程式一次就會執行一次
# lambda 就是一個匿名(沒有名稱、參數)的function，只能用一行寫完

__all__=['update_sqlite_data']



def __download_data() ->list[dict]:
    '''
    下載台鐵即時列車資料
    即時資料網址：https://tdx.transportdata.tw/api/basic/v3/Rail/TRA/TrainLiveBoard?%24top=100&%24format=JSON
    '''
    train_url = 'https://tdx.transportdata.tw/api/basic/v3/Rail/TRA/TrainLiveBoard?%24top=100&%24format=JSON'
    response = requests.get(train_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

def __create_table(conn:sqlite3.Connection): 
    cursor = conn.cursor() 
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '台鐵列車即時狀態'(        
            "id"	INTEGER NOT NULL,
            "車站代碼"	TEXT NOT NULL,
            "車種代碼"	TEXT NOT NULL,
            "車種簡碼"	TEXT,
            "車種名稱_中文"	TEXT,
            "車種名稱_英文"	TEXT,
            "車站代號"	TEXT NOT NULL,
            "車站名稱_中文"	TEXT NOT NULL,
            "車站名稱_英文"	TEXT NOT NULL,
            "列車目前所在之車站狀態	INTEGER NOT NULL,
            "延誤分鐘"	INTEGER,
            "網頁更新時間"	TEXT NOT NULL,
            "資訊下載時間"	DATETIME NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(id,資訊更新時間) ON CONFLICT REPLACE
        ); 
        '''
    ) 
    conn.commit() #執行建立表格

def __update_time():
    time = datetime.now()
    return time

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    sql='''
    REPLACE INTO 台鐵列車即時狀態(車站代碼,車種代碼,車種簡碼,車種名稱_中文,車種名稱_英文,車站代號,車站名稱_中文,車站名稱_英文,列車目前所在之車站狀態,延誤分鐘,網頁更新時間,資訊下載時間)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()

#把資料匯入資料庫sqlite
def update_sqlite_data()->None:
    '''
    下載資料並更新資料庫
    '''
    data = __download_data()
    conn = sqlite3.connect('train.db')
    time = __update_time()

    __create_table(conn)
    for item in data:
        for row in item:
            row['UpdateTime'] = time
        __insert_data(conn, values=[item['TrainNo'], item['TrainTypeID'], item['TrainTypeCode'], item['TrainTypeName:Zh_tw'], item['TrainTypeName:En'], item['StationID'], item['StationName:Zh_tw'],item['StationName:En'],item['TrainStationStatus'],item['DelayTime']])
        
    conn.close() #資料庫必須要關閉
