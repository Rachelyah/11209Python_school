import csv
import sqlite3

__all__=['update_sqlite_data']

def __open_cpbl_data() ->list[dict]:
    
    #讀取新的csv檔案
    pitchings_2022 = 'pitchings_2022.csv'
    try:
        with open (pitchings_2022, mode='r', encoding='utf-8', newline='') as pitchings_file:
            pitchings_dictReader = csv.DictReader(pitchings_file)
            print('讀取成功')
            return list(pitchings_dictReader)
    except Exception as e:
            return print(f'讀取錯誤{e}')


#-------------------建立資料庫--------------------
def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS 'cpbl_pitchings'(        
            "id"	INTEGER,
            "年份"	TEXT NOT NULL,
            "所屬球隊" TEXT NOT NULL,
            "球員編號" TEXT NOT NULL,
            "球員姓名" TEXT NOT NULL,
            "出場數" TEXT NOT NULL,
            "先發次數" INTEGER,
            "中繼次數" INTEGER,
            "勝場數" INTEGER,
            "敗場數" INTEGER,
            "救援成功" INTEGER,
            "中繼成功" INTEGER,
            "有效局數" INTEGER,
            "面對打者數" INTEGER,
            "被安打數" INTEGER,
            "被全壘打數" INTEGER,
            "保送數" INTEGER,
            "三振數" INTEGER,
            "自責分" INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(id, 年份) ON CONFLICT REPLACE
        ); 
        '''
    ) 
    conn.commit() 
    cursor.close()

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    sql='''
    REPLACE INTO cpbl_pitchings(年份, 所屬球隊, 球員編號, 球員姓名, 出場數, 先發次數, 中繼次數, 勝場數, 敗場數, 救援成功, 中繼成功, 有效局數, 面對打者數, 被安打數, 被全壘打數, 保送數, 三振數, 自責分)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()

#把資料匯入資料庫sqlite
def update_sqlite_data()->None:
    '''
    讀取資料並寫入資料庫
    '''
    data = __open_cpbl_data()
    conn = sqlite3.connect('cpbl.db')
    print('寫入環節')
    print(data)
    __create_table(conn)
    for item in data:
        __insert_data(conn, values=[item['Year'], item['Team Name'], item['ID'], item['Name'], item['G'], item['GS'], item['GR'],item['W'], item['L'], item['SV'], item['HLD'], item['IP'], item['BF'], item['H'],item['HR'], item['BB'], item['SO'], item['ER']])
    conn.close() 

#從資料庫中呼叫最新的資料
def lastest_datetime_data()->list[tuple]: 
    conn = sqlite3.connect('cpbl.db')    
    cursor = conn.cursor() 
    #匯入SQL語法
    sql = '''
    SELECT 年份, 所屬球隊, 球員編號, 球員姓名, 出場數, 先發次數, 中繼次數, 勝場數, 敗場數, 救援成功, 中繼成功, 有效局數, 面對打者數, 被安打數, 被全壘打數, 保送數, 三振數, 自責分
    FROM cpbl_pitchings
    '''
    cursor.execute(sql) #執行SQL
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows



#---------------------查詢功能------------------------

def search_sitename(word:str) ->list[tuple]:
    conn = sqlite3.connect('cpbl.db')    
    cursor = conn.cursor() 
    sql = '''
    SELECT 
        年份, 
        所屬球隊, 
        球員編號, 
        球員姓名, 
        出場數, 
        先發次數, 
        中繼次數, 
        勝場數, 
        敗場數, 
        救援成功, 
        中繼成功, 
        有效局數, 
        面對打者數, 
        被安打數, 
        被全壘打數, 
        保送數, 
        三振數, 
        自責分
    FROM cpbl_pitchings
    WHERE 球員姓名 LIKE ?
    GROUP BY 年份, 
        所屬球隊, 
        球員編號, 
        球員姓名, 
        出場數, 
        先發次數, 
        中繼次數, 
        勝場數, 
        敗場數, 
        救援成功, 
        中繼成功, 
        有效局數, 
        面對打者數, 
        被安打數, 
        被全壘打數, 
        保送數, 
        三振數, 
        自責分;
        '''
    
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def team_selected(event, selectVar):
    select_value = selectVar.get()
    print(f"隊伍選擇: {select_value}")
    if select_value == '樂天桃猿':
        print('我走到這了')
        return select_value

def search_by_team(event,word:str):
    print(word) #使用者輸入的文字
    sql=conn = sqlite3.connect('cpbl.db')    
    cursor = conn.cursor() 
    sql = '''
    SELECT 
        年份, 
        所屬球隊, 
        球員編號, 
        球員姓名, 
        出場數, 
        先發次數, 
        中繼次數, 
        勝場數, 
        敗場數, 
        救援成功, 
        中繼成功, 
        有效局數, 
        面對打者數, 
        被安打數, 
        被全壘打數, 
        保送數, 
        三振數, 
        自責分
    FROM cpbl_pitchings
    WHERE 所屬球隊 LIKE ?
    GROUP BY 年份, 
        所屬球隊, 
        球員編號, 
        球員姓名, 
        出場數, 
        先發次數, 
        中繼次數, 
        勝場數, 
        敗場數, 
        救援成功, 
        中繼成功, 
        有效局數, 
        面對打者數, 
        被安打數, 
        被全壘打數, 
        保送數, 
        三振數, 
        自責分;
    '''
    cursor.execute(sql, [f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    print(rows)
    return rows
