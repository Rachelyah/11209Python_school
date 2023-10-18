'''
1. 把台積電的資料放到資料庫
'''

import csv

import sqlite3 
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '台積電股票查詢'(        
            "id"	INTEGER UNIQUE,
            "日期"	TEXT NOT NULL,
            "開盤價" FLOAT NOT NULL,
            "盤中最高價" FLOAT NOT NULL,
            "盤中最低價" FLOAT NOT NULL,
            "收盤價"	FLOAT NOT NULL,
            "調整後收盤價"	FLOAT NOT NULL,
            "成交量"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)   
        ); 
        '''
        ) 
    conn.commit() 

def insert_data(conn, values):
    cursor = conn.cursor()
    sql = '''                  
    INSERT INTO 台積電股票查詢(日期, 開盤價, 盤中最高價, 盤中最低價, 收盤價, 調整後收盤價, 成交量)
        VALUES(?, ?, ?, ?, ?, ?, ?)
    '''   
    cursor.execute(sql, values) 
    conn.commit() 

conn = sqlite3.connect("yf_2330.db") 
create_table(conn)                   

with open('yf_2330.csv') as data:
    data = csv.DictReader(data)
    for item in data: #用for in迴圈寫入資料
        insert_data(conn, [item['Date'], item['Open'], item['High'], item['Low'], item['Close'], item['Adj Close'], item['Volume']])

    