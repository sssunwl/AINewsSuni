# 《AI SaaS 給完全不懂技術的人》課綱

**定位**:不教寫程式,教「為什麼」。每一課都用 SS 自己系統裡的**真實案例**(包括真實事故)當教材。
**這是讀書順序索引,不是第三份內容倉庫**——2026-07-08 發現 `ai-academy/` 已有 CASES(專案案例)+ COLLECT(外部資源,`claude-weekly-collect-digest` 每週自動產生候選)兩套系統在跑,課綱內容一律落地進既有系統,不重寫:
- 「落地」欄標 **cases/xxx**:寫進 `../cases/xxx.md`,同時補齊 `index.html` CASES 陣列裡對應專案的 `lessons:[]`(多課可以共用同一個案例檔,像 WeatherLab 一次收 Server + OAuth 兩課)
- 「落地」欄標 **concepts/**:跨專案的純概念,找不到單一專案可掛,才在 `concepts/` 新寫檔案,格式比照 `cases/ig-resource-organizer.md` 的簡潔風格
- 「落地」欄標 **⏳待CASES**:對應專案(SENA/SnowS、sun-agents 健檢)目前還沒有 CASES 條目,先寫 concepts/,等專案本身夠成熟時再回頭升格成正式 CASES 條目
**產出節奏**:一天一課,由每晚 daily-progress-ledger 的「明日額度建議」排入。
**發佈**:改完 `cases/` 或 `concepts/` 後,照 README 現有流程同步 `index.html` → 複製到 Fablecase repo → push。

## 第一模組:全世界只有五件事(基礎心智模型)

| # | 主題 | 為什麼存在 | 你的真實教材 | 落地 |
|---|------|------|------|------|
| 01 | 輸入→處理→儲存→判斷→輸出 | 所有網站和 App 都是這五件事 | SENA 全架構圖;SnowS 導出流程逐步對應 | concepts/ |
| 02 | Server = 一直開著的電腦 | 服務要 24 小時找得到人 | **WeatherLab 之死**:cron 掛在 Mac 上,沒開機 = 服務斷,還沒人發現 | cases/weatherlab |
| 03 | 本機排程 vs 雲端排程 | 同樣是「定時做事」,死法不同 | WeatherLab(Mac cron,已死)vs okinews(GitHub Actions,天天準時跑) | concepts/(okinews 也還沒進 CASES,一併記一筆) |
| 04 | GitHub = 歷史,不是雲端硬碟 | 改壞了要能回到昨天 | SoSolsunday 積壓一個月沒 commit 的教訓 | concepts/(SoSolsunday 也還沒進 CASES) |
| 05 | GitHub Actions | 讓 GitHub 的電腦幫你定時打工 | 你已有 6 條在跑:ainews / okinews / kujinews / InvestUniS / Polymarket / office tick | concepts/ |

## 第二模組:櫃檯與鑰匙(API 與安全)

| # | 主題 | 為什麼存在 | 你的真實教材 | 落地 |
|---|------|------|------|------|
| 06 | API = 櫃檯 | 你永遠不能走進別人廚房 | SonaSNS 走 Google Sheets API | cases/sona-sheet |
| 07 | API Key = 會員卡 | 櫃檯要知道你是誰 | **2026-07-07 資安事件**:service account 私鑰躺在專案資料夾,健檢時刪除 | concepts/ |
| 08 | OAuth 與 Token 過期 | 不給密碼,只給「可撤銷的授權」 | **WeatherLab invalid_grant 事故**:token 被撤銷,靜默死亡 4 天 | cases/weatherlab(併入 02) |
| 09 | Verify Token vs Access Token | 第一次認親 vs 每天的工作證 | SENA V0.1 A 線:Meta WhatsApp webhook 設定 | ⏳待CASES(SENA) |
| 10 | Secrets 管理 | 鑰匙絕不放在會被看到的地方 | GitHub Secrets + ~/.config/ 慣例;core_rules 資安規則由來 | concepts/ |
| 11 | Hash:為什麼不存明文 | 被偷走也讀不出來 | SnowS:API key 只存 SHA-256,明文只顯示一次 | ⏳待CASES(SnowS) |

## 第三模組:餐廳開張(SENA V0.1 就是實習)

| # | 主題 | 為什麼存在 | 你的真實教材 | 落地 |
|---|------|------|------|------|
| 12 | Webhook = 門鈴 | 不用每秒開門看有沒有客人 | SENA A 線核心:WhatsApp 訊息進來 Meta 主動通知你 | ⏳待CASES(SENA) |
| 13 | Callback URL / DNS / Tunnel | 門鈴要接到你家地址 | Cloudflared 讓 Meta 找到你家的 Mac | ⏳待CASES(SENA) |
| 14 | Backend = 廚房 | 接單、做菜、出餐的地方 | SnowS 的 FastAPI(src/main.py) | ⏳待CASES(SnowS) |
| 15 | Frontend = 店面 | 客人看到的畫面 | SnowS dashboard/index.html、SonaSNS 月曆網站 | cases/sona-sheet(併入 06) |
| 16 | Database = 冰箱 | 明年 John 再來還認得他 | SnowS 的 snows.db(SQLite) | ⏳待CASES(SnowS) |
| 17 | SQLite vs PostgreSQL | 小冰箱夠用就別租冷凍櫃 | SnowS roadmap:多客人並發才換 Postgres | ⏳待CASES(SnowS) |
| 18 | LLM API = 外聘主廚 | AI 回覆的那一步到底發生什麼 | Sophia 回覆核心:Claude API + sena_constitution + 品牌 DNA | ⏳待CASES(SENA) |
| 19 | System Prompt = 憲法 | 為什麼 AI 記得自己是誰 | sena_constitution.json 編譯進 System Prompt | ⏳待CASES(SENA) |
| 20 | 串流與記憶體 | 為什麼大檔案不會撐爆 | SnowS 導出用串流輸出 | ⏳待CASES(SnowS) |

> 12-20 全指向同一個尚未成立的 CASES 條目(SENA/SnowS)。等 V0.1 跑通、SnowS 或 SENA 升格為正式 CASES 項目時,這 9 課會一次變成它的 `lessons:[]`,不用等到那時才動筆——先在 `concepts/` 個別寫,升格時搬過去就好。

## 第四模組:營運與長大

| # | 主題 | 為什麼存在 | 你的真實教材 | 落地 |
|---|------|------|------|------|
| 21 | 部署:Railway / Render / VM | 從「我家 Mac」搬到「租的電腦」 | **InvestUni TG Bot 遷移**(卡 26 天的真實待辦) | cases/investuni |
| 22 | Docker = 打包裝箱 | 去哪台電腦都能跑 | TG Bot 遷移時實際打包一次 | cases/investuni(併入 21) |
| 23 | Rate Limit 與額度 | 所有櫃檯都會限流 | Actions queue 延遲事故、Telegram 限制、Claude 5 小時窗 | concepts/ |
| 24 | MCP | AI 的萬用轉接頭 | 你每天在用:Notion MCP 寫 IG 收藏、Google Drive MCP | concepts/ |
| 25 | 監控與心跳 | 沒有儀表板的工廠會靜默死亡 | **7/7 系統健檢**:三紅燈怎麼抓的、daily-progress-ledger 怎麼設計 | ⏳待CASES(sun-agents 健檢,可能是最快能升格的一筆) |
| 26 | CSV 注入與輸入消毒 | 不要相信任何輸入 | SnowS 防公式注入實作 | ⏳待CASES(SnowS) |

## 規則
- 順序可以跳:當天真實工作碰到哪個概念,就先寫哪課
- 「落地」欄是 cases/ 的課,寫完同步改 `ai-academy/README.md` 索引表的「狀態」欄(待寫教材→完整教材)
- 全部完成前不開新模組、不加新主題

## 進度

| 課 | 狀態 | 落地檔案 | README/index.html 同步 |
|---|---|---|---|
| （尚未開始） | | | |
