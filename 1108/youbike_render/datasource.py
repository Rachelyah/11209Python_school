import requests
import psycopg2
import render_password as rpw

threadRun = True

#次執行緒是否執行(次執行緒：一樣是孫悟空，先放下手邊的事情來做的事情，原本手上的事情會等他)

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
            "更新時間"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
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
    INSERT INTO 台北市youbike(站點名稱,更新時間,行政區,地址,總車輛數,可借,可還)
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
        if threadRun == True:
            __insert_data(conn, values=[item['sna'], item['mday'], item['sarea'], item['ar'], item['tot'], item['sbi'], item['bemp']])
        else:
            break #次執行緒強制執行

    conn.close()

#從資料庫中呼叫最新的資料
def lastest_datetime_data()->list[tuple]: 
    conn = psycopg2.connect(database=rpw.DATABASE, 
                                user=rpw.USER, 
                                password=rpw.PASSWORD, 
                                host=rpw.HOST, 
                                port="5432")   
    cursor = conn.cursor() 
    #匯入SQL語法：抓出1322個站點最新資料（待更新）
    sql = '''
    select a.站點名稱, a.更新時間, a.行政區, a.地址, a.總車輛數, a.可借, a.可還 from 台北市youbike as a 
    join (select distinct 站點名稱,max(更新時間) 更新時間 from 台北市youbike group by 站點名稱) as b
    on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱
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
    select 站點名稱, 更新時間, 行政區, 地址, 總車輛數, 可借, 可還
    from  台北市youbike
    where (更新時間, 站點名稱) in(
	select max(更新時間), 站點名稱
	from 台北市youbike
	group by 站點名稱
	) and 站點名稱 like %s
    '''
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows