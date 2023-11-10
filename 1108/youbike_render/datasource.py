import requests
import psycopg2
import render_password as rpw

def __download_youbike_data()->list[dict]:
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

#------------------建立table--------------------------
def __create_table(conn)->None:   #必須傳回與資料庫連接的物件conn，裡面進行的動作才會與資料庫連線
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間) 
        );
        '''
    )
    conn.commit()
    cursor.close()
    print("create_table成功")

#--------寫入資料，若遇到站點名稱,更新時間相同的資料，不執行任何動作--------------
def __insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    # %s是sql通用的佔位符
    # ON CONFLICT() DO NOTHING遇到括號內欄位資料相同時不執行寫入 
    sql = '''
    INSERT INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借,可還)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (站點名稱, 更新時間) DO NOTHING;
    '''
    cursor.execute(sql,values)    
    conn.commit()
    cursor.close()

#---------更新資料-----------------------
def update_render_data()->None:
    '''
    下載資料並更新資料庫
    '''
    data = __download_youbike_data()
    conn = psycopg2.connect(database=rpw.DATABASE, 
                                user=rpw.USER, 
                                password=rpw.PASSWORD, 
                                host=rpw.HOST, 
                                port="5432") 
    __create_table(conn)
    for item in data:
        __insert_data(conn, values=[item['sna'], item['sarea'], item['mday'], item['ar'], item['tot'], item['sbi'], item['bemp']])
    conn.close()

#從資料庫中呼叫最新的資料
def lastest_datetime_data()->list[tuple]: 
    conn = psycopg2.connect(database=rpw.DATABASE, 
                                user=rpw.USER, 
                                password=rpw.PASSWORD, 
                                host=rpw.HOST, 
                                port="5432")   
    cursor = conn.cursor() 
    #匯入SQL語法
    sql = '''
    SELECT 站點名稱,更新時間,行政區, 地址, 總車輛數, 可借, 可還
    FROM 台北市youbike
    WHERE 更新時間 IN (
	SELECT MAX(更新時間)
	FROM 台北市youbike
	GROUP BY 站點名稱
    );
    '''
    cursor.execute(sql) #執行SQL
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

#查詢第一個關鍵字
#SQL內的要查詢的資訊先寫問號
def search_sitename(word:str) ->list[tuple]:
    conn = psycopg2.connect(database=rpw.DATABASE, 
                            user=rpw.USER, 
                            password=rpw.PASSWORD, 
                            host=rpw.HOST, 
                            port="5432")    
    cursor = conn.cursor() 
    sql = '''
        SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還 
        FROM 台北市youbike
        GROUP BY 站點名稱
        HAVING 站點名稱 LIKE ?
    '''
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows