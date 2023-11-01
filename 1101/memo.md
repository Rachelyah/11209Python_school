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
SELECT 站點名稱, MAX(更新時間) AS 最新時間
FROM 台北市youbike
GROUP BY 站點名稱
```

- 使用Python讀取資料庫
