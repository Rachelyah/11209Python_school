'''
建立moudle，下載youbike2.0的function
'''

import requests


# module裡面可以放function、變數、class
# function內要寫說明用多行文字
# import建議放在最上面，不然放在def裡面每進到程式一次就會執行一次
# lambda 就是一個匿名(沒有名稱、參數)的function，只能用一行寫完

def download_youbike_data():
    '''
    下載台北市youbike2.0的資料
    即時資料網址：https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    # 
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

    response = requests.get(youbike_url) #使用requests.get方法(使用requset.request也可以，但就要寫兩個參數*方法+連結)
    if requests.status_codes == 200:
        #print('下載成功')
        raise Exception('下載失敗') 
    else:
        raise Exception('下載失敗') #傳出錯誤訊息給主程式
    #可以參考標準函式庫的例外說明，module只負責傳出錯誤(處理錯誤在主程式進行)，如果print字串系統無法辨認是否錯誤&例外，因此用Exception說明