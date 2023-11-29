#### [文件](https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates)

#### Jinja的變數表現法
- {% ... %} 是用於執行語句的標記，用來包裹條件語句、迴圈等。

- {{ ... }} 是用於表達式的標記，用來顯示變數或執行表達式。

- {# ... #} 是用於註釋的標記，這部分的內容不會被輸出到最終的模板結果中。

#### boostrap
- [boostrap](https://getbootstrap.com/docs/5.3/layout/breakpoints/)

#### docker
- [Docker](https://philipzheng.gitbook.io/docker_practice/basic_concept/repository)

#### Jinja
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)

#### blueprint
- [blueprint](https://medium.com/seaniap/python-web-flask-blueprints-%E8%A7%A3%E6%B1%BA%E5%A4%A7%E6%9E%B6%E6%A7%8B%E7%9A%84%E7%B6%B2%E7%AB%99-1f9878312526)

#### boostraps breakpoints 自適應網頁中斷點的尺寸跟縮寫
- [breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/)
- none 手機直的
- sm 手機橫的
- md 平板
- lg 一般螢幕
- xl 大螢幕
- xxl 超大電競螢幕

```
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// X-Large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }

// XX-Large devices (larger desktops, 1400px and up)
@media (min-width: 1400px) { ... }
```

#### container
- 除了breakpoints直接下尺寸之外，也可以寫container-(容器名稱)直接寫設定名稱

#### row
- 每一個row裡面可以放12個col，可以分配每一個盒子需要占用的比例e.g. col-5，col-7，如果你一個row裡面沒有占滿12個col，剩下的空間會被空著
- 也有一種寫法是，在col-5前後都放col，那剩下的空間會在兩個col內被平分，會是剛好的勒奧
- 也可以搭配justify-contect，設定在class，設定row裡面的col要擺在哪個位置
- <div class="col-5 five"> <!--一欄固定五個，其它給上下的class分配，因為上下都是col，所以一定會平均分配，左右兩邊一樣大-->

#### 假圖套件
- Lorem Picsum photos snippets

#### 讓flask網頁連結至postgre資料庫，並透過pandas把資料整理成圖表
- 把之前youbike的datasource.py、password.py檔案放到bs資料夾中
- 要注意引用時要寫from . import 從根目錄讀取
- 寫入bootstrap.py的test方法中，新版的python可以在變數前面宣告資料類型

#### 表格table標籤
- table 表格本體
    - thead 有點像是盒子的概念
    - tbody 有點像是盒子的概念
    - tfoot 有點像是盒子的概念
        - tr 垂直列(row)
        - td 水平欄(column)