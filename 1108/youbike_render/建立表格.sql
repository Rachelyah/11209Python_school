select a.* from 台北市youbike a
 join (select distinct 站點名稱,max(更新時間) 更新時間
from 台北市youbike group by 站點名稱) as b
 on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱--建立table
CREATE TABLE IF NOT EXISTS 台北市youbike(        
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT NOT NULL,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間)
        ); 

--查詢table
SELECT * FROM 台北市youbike

--刪除table&資料
DROP TABLE 台北市youbike

delete from 台北市youbike

--查詢table
SELECT * FROM 台北市youbike

--如果有重複資料，更新該筆資料UPDATE SET的資訊
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_臺大明達館北側(員工宿舍)','臺大公館校區','2023-11-10 09:54:16','明達館北側前空地',100,10,20)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 18, 
      可借 = 0,
	  可還 = 18;

--如果有重複資料，不寫入這筆資料(ON CONFLICT DO NOTHING)
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',100,10,20)
ON CONFLICT (站點名稱, 更新時間) DO NOTHING;

--查詢
SELECT * 
FROM 台北市youbike
WHERE 站點名稱='YouBike2.0_臺大明達館北側(員工宿舍)'

--查詢1322個站點最新更新時間的資訊(seld join)
/*
把資料表所有欄位資料集定義為a，子查詢抓出不重複的各站點最新時間定義為b
把資料a跟b inner join，只保留*/

select a.* from 台北市youbike as a --把資料表所有欄位的資料集定義為a
 join (select distinct 站點名稱,max(更新時間) 更新時間 from 台北市youbike group by 站點名稱) as b --把子查詢結果定義為b
 on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱


--原本的想法，但這樣無法抓到最新時間，會超過1322筆資料
select distinct 站點名稱,max(更新時間) 更新時間,行政區, 地址, 總車輛數, 可借, 可還 from 台北市youbike group by 站點名稱,行政區, 地址, 總車輛數, 可借, 可還
