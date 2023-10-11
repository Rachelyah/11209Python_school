#要執行的檔案會寫if __name__ == "__main__"
#我的下載def寫在dataSource這個module裡面
#目前都沒有把檔案建立及寫入在本地端，每次執行我都是透過download()去網路上下載一次資料，酷喔

import dataSource  

def main():
    try:
        data_list = dataSource.download() #我呼叫dataSource裡面dowload()這個method
    except Exception as e:     
        print(f'錯誤:{e}') 
    else:
        for row in list(data_list): 
            print(row)
            
if __name__ == "__main__":
    main()                  #很多應用程式的執行點都在main()