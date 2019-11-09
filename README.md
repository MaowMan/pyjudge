# pyjudge
 輕量級的離線程式批改系統  
 以 MIT License 發行
# 專案介紹
 由python編寫的簡易程式批改系統，適用於教職人員批改作業、測驗等。  
 以資料夾區分不同的測驗，批改之後自動輸出csv成績檔案  
# 執行需求
 [Python 3](https://www.python.org/)
 編寫時版本為3.8  
 其餘皆為Python 標準函式庫
# 如何使用
 執行 `Setup_GUI.py`配置系統相關參數及文件  
 執行`Main.py` 開始批改
 ***
 *建議完整了解原始碼才使用以下方法*  
 手動修改`./Config/MainConfig.json` 更改judge系統目標測驗資料夾  
 如何配置文件可以參考`./Template/`中的範例檔案  
 執行`Main.py` 開始批改
# 批改檔案支援
 目前僅支持 Python(.py)
# 檔案說明
 `./Template/`範例測驗資料夾  
 `./Scripts/`類別及函式  
 `./Config/` 程式所需設定檔
# 備註
 如果視窗不正常關閉可能導致tkinter無法正確運作  
 重新開機即可解決這一問題

