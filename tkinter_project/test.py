import sqlite3
import csv

'''
ID: 球員編號，用於識別球員的唯一標識。
Name: 球員姓名，表示投手的名稱。
Team Name: 球隊名稱，表示所屬的球隊名稱。
G: 出場數（Games Played），表示投手出場的比賽場次。
GS: 先發次數（Games Started），表示投手擔任先發投手的次數。
GR: 中繼次數（Games in Relief），表示投手作為中繼投手的次數。
CG: 完投次數（Complete Games），表示投手完成整場比賽的次數。
SHO: 完封次數（Shutouts），表示投手完成比賽且對手一分未得的次數。
W: 勝利次數（Wins），表示投手在比賽中獲得的勝利次數。
L: 失敗次數（Losses），表示投手在比賽中遭遇的敗戰次數。
SV: 救援成功次數（Saves），表示投手成功完成救援的次數，即在比賽結束前保護領先優勢。
HLD: 中繼成功次數（Holds），表示投手成功完成中繼的次數，即在比賽中繼投手的表現。
IP: 有效局數（Innings Pitched），表示投手投球的有效局數，通常以局（Innings）為單位。
BF: 面對打者數（Batters Faced），表示投手面對的總打者數。
NP: 投球總數（Number of Pitches），表示投手投球的總次數。
H: 被安打數（Hits Allowed），表示投手被對手擊出的安打數。
HR: 被全壘打數（Home Runs Allowed），表示投手被擊出的全壘打數。
BB: 保送數（Bases on Balls），表示投手送出的保送數。
IBB: 故意四壞球數（Intentional Bases on Balls），表示投手有意地故意送出的保送數。
HBP: 觸身球數（Hit By Pitch），表示投手觸身球的次數，即投手將球投向打者並擊中其身體。
SO: 三振數（Strikeouts），表示投手投出的三振次數。
WP: 暴投數（Wild Pitches），表示投手投出的暴投次數。
BK: 犯規球數（Balks），表示投手犯下的犯規次數。
R: 被得分數（Runs Allowed），表示投手被對手得分的總次數。
ER: 自責分（Earned Runs），表示投手失控所導致的得分，不包括因失誤或其他原因導致的得分。
GO: 滾地出局（Ground Outs），表示投手由對方擊出的滾地球導致的出局次數。
'''

#建立csv檔案路徑
csv_file = 'pitchings.csv'

# 建立 SQLite 資料庫連接
conn = sqlite3.connect('cpbl_data.db')
cursor = conn.cursor()

#def __create_table_battings(conn:sqlite3.Connection): 
cursor = conn.cursor()
cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS 'cpbl_pitchings'(        
            "id"	INTEGER,
            "更新時間" TEXT NOT NULL,
            "所屬球隊"	TEXT NOT NULL,
            "球員編號" TEXT NOT NULL,
            "球員姓名"	TEXT NOT NULL,
            "出場數"	TEXT NOT NULL,
            "先發次數"	INTEGER,
            "中繼次數"	INTEGER,
            "完投次數"	INTEGER,
            "完封次數"	INTEGER,
            "勝場數"	INTEGER,
            "敗場數"	INTEGER,
            "救援成功"	INTEGER,
            "中繼成功"	INTEGER,
            "有效局數" INTEGER,
            "面對打者數"	INTEGER,
            "被安打數"	INTEGER,
            "被全壘打數"	INTEGER,
            "保送數"	INTEGER,
            "故意四壞球數"	INTEGER,
            "三振數"	INTEGER,
            "自責分" INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(id, 更新時間) ON CONFLICT REPLACE
        ); 
        '''
    ) 
conn.commit() 

#def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
cursor = conn.cursor()

    # 讀取 CSV 檔案，寫入資料庫
with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
                # 在每一行的字典中添加 '更新時間' 欄位
                row['更新時間'] = '2022'

            # 插入資料庫
                cursor.execute('''
                    INSERT INTO cpbl_pitching(
                        更新時間, 所屬球隊, 球員編號, 球員姓名, 出場數, 先發次數, 中繼次數, 完投次數, 完封次數, 勝場數, 敗場數, 救援成功, 中繼成功, 有效局數, 面對打者數, 被安打數, 被全壘打數, 保送數,故意四壞球數 ,三振數, 自責分
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (row['更新時間'], row['Team Name'], row['ID'], row['Name'], row['G'], row['GS'],
            row['GR'], row['CG'], row['SHO'], row['W'], row['L'],
            row['SV'], row['HLD'], row['IP'], row['BF'], row['H'], row['HR'], row['BB'],
            row['IBB'], row['SO'], row['ER']
            ))

conn.commit()
conn.close()


