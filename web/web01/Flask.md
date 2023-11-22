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
