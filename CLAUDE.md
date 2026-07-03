# Claude Instructions — AINewsSuni

這個 repo 除了 AI 新聞摘要機器人本體，也是 SS 手機隨手丟連結的「快速收集入口」。

## 個人資源整理（IG / 網頁 / 課程連結收集）

當 SS 貼一個連結給你（IG 貼文、一般網頁文章、線上課程）：

1. **先試著用 WebFetch 讀取內容**
   - 一般網頁/課程頁面：通常讀得到，直接判斷分類、寫重點摘要，完整整理
   - Instagram 連結：大多需要登入才能看到內容，WebFetch 會失敗——**這是預期中的限制**，不用一直重試

2. **寫入 Notion 資料庫「IG 收藏整理」**
   - 資料庫網址：https://app.notion.com/p/b24c50f9af1945d2883ef7356e19094a （若 MCP 有 fetch 工具，用網址或 data source id `collection://64777f8b-6b24-4f1d-ba0f-d46df2ad6c43` 存取）
   - 欄位：標題、連結、分類（Claude Code 教學/餐廳/線上課程/文章/網頁/其他）、媒體類型（影片/圖片/圖文）、狀態、驗證狀態、平台、課程進度、重點摘要、地點
   - **讀得到內容**：正常填寫所有欄位，狀態填「已整理」
   - **讀不到內容（多半是 IG）**：標題用網址或 SS 當下順口描述的內容代替，分類先用猜測或問 SS，**狀態填「待整理」**，重點摘要留空或寫「待查證內容」——不用因為讀不到就拒絕記錄，先讓連結進資料庫，等每週 review 再處理

3. **不用勉強做超出能力範圍的事**：雲端 session 沒有 Claude in Chrome，讀不到需要登入的內容是正常現象，如實記錄「待整理」即可，不要編造內容或猜測摘要當真的寫進去。

## 每週 Review 機制

SS 每週會在本機（有 Claude in Chrome 的 Sun session）做 review，把「狀態＝待整理」的項目（主要是 IG）逐一打開、寫摘要、改成「已整理」，並視需要做「彙整」（例如某月餐廳推薦、某主題教學總結）。你不需要主動做這件事，這是 Sun 那邊的工作。

## 其他

本 repo 也是 AINewsSuni（AI 新聞摘要機器人）本體所在，詳見 [README.md](README.md)；AI 學院教學素材在 [ai-academy/](ai-academy/README.md)。
