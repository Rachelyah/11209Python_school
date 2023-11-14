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