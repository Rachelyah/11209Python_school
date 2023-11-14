--建置pm2.5資料表
CREATE TABLE  IF NOT EXISTS taiwan_pm25(
   "id"	SERIAL,
   "測站名稱"	TEXT NOT NULL,
   "縣市名稱"	TEXT NOT NULL,
   "pm25"	TEXT NOT NULL,
   "資料建置時間"	TEXT,
   PRIMARY KEY("id"),
    UNIQUE(測站名稱,資料建置時間) 
        );
--查詢		
select * from taiwan_pm25

--抓出各測站最新資訊
select a.測站名稱, a.縣市名稱, a.pm25, a.資料建置時間 from taiwan_pm25 as a --把資料表所有欄位的資料集定義為a
 join (select distinct 測站名稱,max(資料建置時間) 資料建置時間 from taiwan_pm25 group by 測站名稱) as b --把子查詢結果定義為b
 on a.資料建置時間=b.資料建置時間 and a.測站名稱=b.測站名稱
 
--刪除資料表
drop table taiwan_pm25