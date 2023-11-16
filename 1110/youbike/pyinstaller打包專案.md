#### [pyinstaller打包專案流程](https://vuarnet0318.medium.com/learn-python-%E6%89%93%E5%8C%85%E4%BD%A0%E7%9A%84python%E7%A8%8B%E5%BC%8F-pyinstaller%E5%9F%BA%E7%A4%8E%E7%AF%87-ea4e0400d2ed)

1. 安裝pyinstaller套件
```
pip install pyinstaller
```

2. 開啟終端機，執行你要打包的檔案，記得所有檔案要放在同一個資料夾裡

```
pyinstaller -w index.py (-w代表只顯示window的內容，不會出現終端機)
```

3. 執行完成後，會出現build、dist等資料夾
    - build資料夾不重要可忽略，是編譯執行檔出現的檔案
    - dist裡面會有exe的可執行檔案(Mac是pkg檔)

4. 把整個dist檔案打包放到桌面，就是一個完整的應用程式(Mac好像可以只打包pkg檔案)

5. 注意這些東西不要上傳到GitHub，專案資料夾的檔案打包複製完之後就可以刪除