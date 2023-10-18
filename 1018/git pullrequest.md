#### git pullrequest
- 他是一個git repo(open source)，所有人都可以共同開發
- 你可以共同開發，也可以「fork」裡面的資料夾
- (fork：把一份相同的專案放在你的帳號之下，讓你能夠公開對這專案做變更，做為一個以更開放的方式來參與專案，原本專案的擁有者必須同意你的修改，才能將你的修改傳回原始的repo)
    1. 到你要fork的專案資料夾，點選fork，create到自己的GitHub中
    2. 回到VS CODE，透過GitHub存放庫Clone你fork的repo下來(自己GitHub中的repo)
    3. 修改後直接上傳commit(這時候都在自己的GitHub)
    4. 回到你的repo -> pull requests -> create pull requests ->  新增你的說明 -> 送出請求
    5. 專案管理者審核需求& merge 所有的修改到原始專案中
    6. 回到你的repo，update原始專案的更新到自己的repo中
    7. 更新自己VS CODE的內容到最新版
    8. 當你在跟大家一起編輯同一個檔案時，很容易有衝突問題，要隨時點選VS CODE左下角的main更新