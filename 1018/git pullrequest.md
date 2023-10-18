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
    9. 如果不要太麻煩(每次都要去雲端手動更新) **待研究目前是失敗**
        - 在自己的repo資料夾終端機中開啟default
        - gh repo set-default(選擇自己的repo，不是原始檔案的repo)
        - gh repo sync (自動更新)
        - 專案擁有者如何自動同意merge的commit？
        - 本地端的repo如何自動更新最新檔案(與專案擁有者連動？)
        [說明文件](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)
        [auto merge Doc](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

- 如果上傳遇到衝突，
- git config pull.rebase false