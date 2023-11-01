--查詢指定欄位中最新資料
SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還 
FROM 台北市youbike
GROUP BY 站點名稱
HAVING 站點名稱 LIKE '%松山%'  --搜尋關鍵字
AND 站點名稱 LIKE '%家商%' --追加搜尋關鍵字
AND 可借 > 0