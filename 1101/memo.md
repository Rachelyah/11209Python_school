Timer()會在背景自動更新，如果要停止，要寫t.canel()強制關閉，tkinter也有內建的同樣工具after
![Alt text](image.png)

- Recursion遞迴：自己的def裡面又呼叫自己
- [參考](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-11ed5d300d3d)

#### SQLite語法(在視窗中按執行SQL)
- 查詢指定欄位，並省略不重複的資料

```
SELECT DISTINCT 站點名稱
FROM 台北市youbike
```

- 查詢指定欄位中最新資料
```
SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還 
FROM 台北市youbike
GROUP BY 站點名稱
```
- 把資料庫資料用Python讀取，並透過tkinter匯入視窗中
    1. 建立datasource.py，確定資料庫下載+定期自動更新的function
    2. 建立資料庫SQL語法
    3. 建立視窗&樹狀表格