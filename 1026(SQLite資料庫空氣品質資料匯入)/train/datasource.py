
import requests
import sqlite3
from datetime import datetime

__all__=['update_sqlite_data']


def __download_data() ->list[dict]:
    library_url = 'https://seat.tpml.edu.tw/sm/service/getAllArea'
    response = requests.get(library_url)
    response.raise_for_status()
    print('下載成功')
    data = response.json()
    print(data)
    return data

def __create_table(conn:sqlite3.Connection): 
    cursor = conn.cursor() 
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '台北市圖書館即時座位'(        
            "id"	INTEGER NOT NULL,
            "區域編號"	TEXT NOT NULL,
            "分館名稱"	TEXT NOT NULL,
            "樓層"	TEXT,
            "區域名稱"	TEXT,
            "剩餘座位數" INTEGER NOT NULL,
            "總座位數"	INTEGER NOT NULL,
            "資訊更新時間"	TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(區域編號) ON CONFLICT REPLACE
        ); 
        '''
    ) 
    conn.commit() #執行建立表格

def __update_time():
    time = datetime.now()
    return time

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    time = datetime.now()
    sql='''
    REPLACE INTO 台北市圖書館即時座位(區域編號,分館名稱,樓層,區域名稱,剩餘座位數,總座位數,資訊更新時間)
        VALUES(?,?,?,?,?,?,?)
    '''
    values.append(time)
    cursor.execute(sql,values)
    conn.commit()

#把資料匯入資料庫sqlite
def update_sqlite_data()->None:
    '''
    下載資料並更新資料庫
    '''
    data = __download_data()
    conn = sqlite3.connect('台北市圖書館座位.db')
    __create_table(conn)
    for item in data:
        __insert_data(conn, values=[item['areaId'], item['branchName'], item['floorName'], item['areaName'], item['freeCount'], item['totalCount']])
    
    conn.close() #資料庫必須要關閉
