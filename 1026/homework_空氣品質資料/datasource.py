'''
1. 建立moudle，下載環境部空氣品質資料的function
'''

import requests
import sqlite3

# module裡面可以放function、變數、class
# function內要寫說明用多行文字
# import建議放在最上面，不然放在def裡面每進到程式一次就會執行一次
# lambda 就是一個匿名(沒有名稱、參數)的function，只能用一行寫完

__all__=['update_sqlite_data']

def __download_data() ->list[dict]:
    '''
    下載台北市youbike2.0的資料
    即時資料網址：https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=133f5725-c027-46fd-9aca-d97096ead024
    '''
    
    air_quality_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=133f5725-c027-46fd-9aca-d97096ead024'

    response = requests.get(air_quality_url) 
    response.raise_for_status()
    print('下載成功')
    return response.json() 

def __create_table(conn:sqlite3.Connection): 
    cursor = conn.cursor() 
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '環境部空氣品質'(        
            "id"	INTEGER,
            "測站名稱"	TEXT NOT NULL,
            "測站英文名稱"	TEXT NOT NULL,
            "空品區"	TEXT NOT NULL,
            "城市"	TEXT NOT NULL,
            "鄉鎮"	TEXT NOT NULL,
            "測站地址"	TEXT NOT NULL,
            "經度"	TEXT NOT NULL,
            "緯度"	TEXT NOT NULL,
            "測站類型"	TEXT,
            "測站編號"	TEXT,
            "資訊更新時間"	DATETIME,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(站點名稱,更新時間) ON CONFLICT REPLACE
        ); 
        '''
    ) 
    conn.commit() #執行建立表格

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    #[INSERT OR]REPLACE INTO TABLE(COLUMN_LIST) VALUES
    #輸入資料，如果已經有前一筆資料就用新的重新覆蓋，如果沒有的話就輸入在後面
    sql='''
    REPLACE INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借,可還)
        VALUES(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()

#把資料匯入資料庫sqlite
def update_sqlite_data()->None:
    '''
    下載資料並更新資料庫
    '''
    data = __download_youbike_data()
    conn = sqlite3.connect('youbike.db')
    __create_table(conn)
    for item in data:
        __insert_data(conn, values=[item['sna'], item['sarea'], item['mday'], item['ar'], item['tot'], item['sbi'], item['bemp']])
    conn.close() #資料庫必須要關閉
