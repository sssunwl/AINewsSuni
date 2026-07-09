# 《AI SaaS 給完全不懂技術的人》課綱

**定位**:不教寫程式,教「為什麼」。每一課都用 SS 自己系統裡的**真實案例**(包括真實事故)當教材——這是別的課程抄不走的差異化。
**產出節奏**:一天一課,由每晚 daily-progress-ledger 的「明日額度建議」排入;每課產出一篇 Learning Record(模板見 `templates/learning_record.md`),存 `lessons/NN-主題.md`。
**發佈**:課文完成後同步到 Fablecase 網站(分工:這裡是源檔與草稿,Fablecase 是公開版)。

## 第一模組:全世界只有五件事(基礎心智模型)

| # | 主題 | 為什麼存在(一句話) | 你的真實教材 |
|---|------|------|------|
| 01 | 輸入→處理→儲存→判斷→輸出 | 所有網站和 App 都是這五件事 | SENA 全架構圖;SnowS 導出流程逐步對應 |
| 02 | Server = 一直開著的電腦 | 服務要 24 小時找得到人 | **WeatherLab 之死**:cron 掛在 Mac 上,Mac 沒開機 = 服務斷,還沒人發現 |
| 03 | 本機排程 vs 雲端排程 | 同樣是「定時做事」,死法不同 | WeatherLab(Mac cron,已死)vs okinews(GitHub Actions,天天準時跑) |
| 04 | GitHub = 歷史,不是雲端硬碟 | 改壞了要能回到昨天 | SoSolsunday 積壓一個月沒 commit 的教訓;每日對帳靠 git log 重建進度 |
| 05 | GitHub Actions | 讓 GitHub 的電腦幫你定時打工 | 你已有 6 條在跑:ainews / okinews / kujinews / InvestUniS / Polymarket / office tick |

## 第二模組:櫃檯與鑰匙(API 與安全)

| # | 主題 | 為什麼存在 | 你的真實教材 |
|---|------|------|------|
| 06 | API = 櫃檯 | 你永遠不能走進別人廚房 | SonaSNS 走 Google Sheets API;APIdatabase 已收錄 HKO 天氣/KMB 巴士 |
| 07 | API Key = 會員卡 | 櫃檯要知道你是誰 | **2026-07-07 真實資安事件**:service account 私鑰躺在專案資料夾,健檢時刪除 |
| 08 | OAuth 與 Token 過期 | 不給密碼,只給「可撤銷的授權」 | **WeatherLab invalid_grant 事故**:token 被撤銷,自動化靜默死亡 4 天 |
| 09 | Verify Token vs Access Token | 第一次認親 vs 每天的工作證 | SENA V0.1 A 線:Meta WhatsApp webhook 設定(學完立刻真的用) |
| 10 | Secrets 管理 | 鑰匙絕不放在會被看到的地方 | 你的既有慣例:GitHub Secrets + ~/.config/;core_rules 資安規則的由來 |
| 11 | Hash:為什麼不存明文 | 被偷走也讀不出來 | SnowS 已實作:API key 只存 SHA-256,明文只顯示一次 |

## 第三模組:餐廳開張(SENA V0.1 就是實習)

| # | 主題 | 為什麼存在 | 你的真實教材 |
|---|------|------|------|
| 12 | Webhook = 門鈴 | 不用每秒開門看有沒有客人 | SENA A 線核心:WhatsApp 訊息進來 Meta 主動通知你 |
| 13 | Callback URL / DNS / Tunnel | 門鈴要接到你家地址 | 用 Cloudflared 讓 Meta 找到你家的 Mac(V0.1 實作) |
| 14 | Backend = 廚房 | 接單、做菜、出餐的地方 | SnowS 的 FastAPI(src/main.py)就是,已經在跑 |
| 15 | Frontend = 店面 | 客人看到的畫面 | SnowS dashboard/index.html、SonaSNS 月曆網站 |
| 16 | Database = 冰箱 | 明年 John 再來還認得他 | SnowS 的 snows.db(SQLite);對話儲存設計 |
| 17 | SQLite vs PostgreSQL | 小冰箱夠用就別租冷凍櫃 | SnowS roadmap 已寫明:多客人並發才換 Postgres(反過度工程的活教材) |
| 18 | LLM API = 外聘主廚 | AI 回覆的那一步到底發生什麼 | Sophia 回覆核心:Claude API + sena_constitution + 品牌 DNA |
| 19 | System Prompt = 憲法 | 為什麼 AI 記得自己是誰 | sena_constitution.json 編譯進 System Prompt 的設計 |
| 20 | 串流與記憶體 | 為什麼大檔案不會撐爆 | SnowS 導出用串流輸出(已實作) |

## 第四模組:營運與長大

| # | 主題 | 為什麼存在 | 你的真實教材 |
|---|------|------|------|
| 21 | 部署:Railway / Render / VM | 從「我家 Mac」搬到「租的電腦」 | **InvestUni TG Bot 遷移**(卡 26 天的真實待辦,學完順手做完) |
| 22 | Docker = 打包裝箱 | 去哪台電腦都能跑 | TG Bot 遷移時實際打包一次 |
| 23 | Rate Limit 與額度 | 所有櫃檯都會限流 | Actions queue 延遲 2-4h 事故、Telegram 限制、Claude 5 小時窗 |
| 24 | MCP | AI 的萬用轉接頭 | 你每天在用:Notion MCP 寫 IG 收藏、Google Drive MCP |
| 25 | 監控與心跳 | 沒有儀表板的工廠會靜默死亡 | **7/7 系統健檢完整案例**:三紅燈怎麼抓的、daily-progress-ledger 怎麼設計 |
| 26 | CSV 注入與輸入消毒 | 不要相信任何輸入 | SnowS 防公式注入實作(`=`開頭加`'`) |

## 規則
- 順序可以跳:當天真實工作碰到哪個概念,就先寫哪課(真實優先於課綱順序)
- 每課寫完在下表登記;全部完成前不開新模組、不加新主題(防止課綱膨脹成又一個爛尾架構)

## 進度

| 課 | 狀態 | 檔案 | 發佈到 Fablecase |
|---|---|---|---|
| （尚未開始） | | | |
