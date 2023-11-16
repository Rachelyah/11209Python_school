### 需求描述
- 下載url：'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=133f5725-c027-46fd-9aca-d97096ead024'
- 資料來源：[環境部 /aqx_p_02 細懸浮微粒資料（PM2.5）](https://data.moenv.gov.tw/swagger/#/)
- ![Alt text](image.png)

- 這個專案只需要寫一個py檔，不需要寫視窗，也不用分index跟datasource
- 所以固定執行不一定要用Timer來寫
- 可以用while迴圈搭配time.sleep()來寫＞暫停多久時間後再執行一次