- 我建立的變數可以在哪個namespace內使用？
    - if, while, for迴圈建立的變數，是全域變數，可以在整個index.py使用
    - 如果是在個別的function內建立的變數，就只能在function內有效
    - 如果已經有全域變數a=10，後來在funtion內寫a=5，那他在function內的值就會變成5
    - 如果要全域變數在funtion內也都可以使用，要寫global a，這樣就算在function內把a的值給為7，出來之後在其他區塊執行，a也會=7

- 如果你只是要在function裡面使用全域變數，直接寫a就好
- 如果要給值，意思就是有a=，那就必須在function的一開始先寫global a