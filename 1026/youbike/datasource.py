'''
建立moudle，下載youbike2.0的function
'''

import requests
import sqlite3

# module裡面可以放function、變數、class
# function內要寫說明用多行文字
# import建議放在最上面，不然放在def裡面每進到程式一次就會執行一次
# lambda 就是一個匿名(沒有名稱、參數)的function，只能用一行寫完

__all__=['update_sqlite_data']

def __download_youbike_data() ->list[dict]:
    '''
    下載台北市youbike2.0的資料
    即時資料網址：https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

    response = requests.get(youbike_url) #使用requests.get方法(使用requset.request也可以，但就要寫兩個參數*方法+連結)
    response.raise_for_status()
    print('下載成功')
    #如果使用raise_for_status就不用寫下面的這段，會自動傳回下載結果正確or錯誤給主程式
    return response.json() #把結果傳回主程式，也有內建的raise檢查機制(當檔案不是json時)

    #if requests.status_codes == 200:
        #print('下載成功')
        #raise Exception('下載失敗') 
    #else:
        #raise Exception('下載失敗') #傳出錯誤訊息給主程式
    #可以參考標準函式庫的例外說明，module只負責傳出錯誤(處理錯誤在主程式進行)，如果print字串系統無法辨認是否錯誤&例外，因此用Exception說明

#建立資料庫&欄位，function名稱加入__表示這是我內部使用的
def __create_table(conn:sqlite3.Connection): #資料型別是sqlite3.Connection
    cursor = conn.cursor() #cursor()才可以執行sql語法
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '台北市youbike'(        
            "id"	INTEGER,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT NOT NULL,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
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
