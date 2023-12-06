import requests
import psycopg2
from . import render_password as rpw

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