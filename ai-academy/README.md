# AI 學院

用自己真實在跑的 AI 應用專案當教材，教別人怎麼跟 AI 協作。

**網站原始檔已搬到 `aisuni/`（2026-09-21 合併）**：學院主頁、公開案例筆記、每日 AI 新聞頁都在工作區頂層 `aisuni/`（repo [sssunwl/aisuni](https://github.com/sssunwl/aisuni)，線上 <https://sssunwl.github.io/aisuni/>），**直接改那邊、push 即上線**，不再有「改這裡再複製過去」的鏡像流程。舊網址 `sssunwl.github.io/AINewsSuni/` 會自動轉到 `aisuni/news/`。

這個資料夾現在只放**不公開**的東西：案例範本與草稿（`cases/_TEMPLATE.md`、`cases/_drafts/`）、付費商品 AI OS 入門包（`aios-starter-kit/`）、課程素材（`course-ai-saas/`）、收集箱候選（`collect-inbox.md`）。案例寫完要公開時，把 md 放進 `aisuni/cases/`。

**收集箱週報（排程自動化）**：每週一 09:00 排程任務（`claude-weekly-collect-digest`）掃描來源、產最多 5 筆候選寫進 [collect-inbox.md](collect-inbox.md)，**只進候選區、不自動上站**。沒審核的候選留著併入每週 review。狀態：候選 / 已上站 / 略過。

**⚠️ Notion 才是 AI 工具/教學收藏的唯一真相來源，COLLECT 是它的精選公開版**——SS 手機隨手丟連結進 Notion「IG 收藏整理」（分類「Claude Code 教學」「其他」），這裡的週報收集箱是同一種內容的公開出口。2026-07-08 發現這條規則沒有真正落實：Notion 裡已有 Agent Sprite Forge、OpenMontage、Codex & Claude Code 實戰分享等 5 筆從沒被同步成 COLLECT 公開版。

**已修：`claude-weekly-collect-digest` 現在跑兩軌**（見任務檔 `~/.claude/scheduled-tasks/claude-weekly-collect-digest/SKILL.md`）：
- **A 軌**：跟原本一樣，掃外部來源找新東西，最多 5 筆
- **B 軌**：直接查 Notion「IG 收藏整理」，把「分類=Claude Code教學/其他 且 狀態=已整理 且 驗證狀態=已查證屬實」的項目當成「私人收藏已成熟，建議公開」的候選——這個判斷不是新發明的品質標準，就是沿用 SS 在每週 review 時已經填好的 狀態/驗證狀態 欄位，B 軌只是把「已經審過的東西」接到公開流程，不重新審內容好壞

兩軌都只進 [collect-inbox.md](collect-inbox.md) 候選區,SS 回「上 N」才真的公開。下週一(下次排程執行)B 軌會自動把現有 5 筆裡「已查證屬實」的部分列出來。

SS 回「上 N」之後，當時的 session 必須**一次做完下面四件事**，不可以只做前兩項——上站跟 Notion 分開做是資料分裂的根源，之前已經因為漏做而被抓到過一次：

1. 把該筆加進 `aisuni/index.html` 的 `COLLECT` 陣列
2. 在 `aisuni/` commit push（Pages 自動重建）
3. **寫進 Notion「IG 收藏整理」資料庫**（同一個庫，分類選「Claude Code 教學」）——這是所有收集項目的唯一真相來源，網站只是精選公開版，兩邊都要有
4. 把 `collect-inbox.md` 裡該筆的狀態從「候選」改成「已上站」

每個案例對應 `/Users/sws/Sun/Claude` 底下的一個實際專案（例如 AINewsSuni、SonaSNS-Platform、WeatherLab...），記錄的不只是「做出了什麼」，而是**需求 → 設計討論 → 取捨決策**的完整過程。

### 2026-09-08 工作紀錄

完成 CapyChill 長片案例教材並首次把 `cases/` 深度筆記同步到公開的 `aisuni` 網站；部署 repo 的兩筆 commit 已推送，並修正舊 Fablecase Pages 連結。另已在本機完成「個人 AI OS 入門包」六份 Markdown 內容、首頁入口與 Gumroad 商品文案，但 Gumroad 商品網址仍是佔位值，AINewsSuni 與 Gumroad 兩邊的變更也尚未提交；下一步是建立正式商品、替換網址，驗收下載內容與頁面後再提交／發布。

### 2026-07-21 工作紀錄

今日更新 AI Academy 首頁的 AI OS 入門內容與案例呈現，並新增 `aios-starter-kit/01-mega-prompt.md`，讓使用者能以互動問答建立第一個 Agent 藍圖；同時把案例專案根路徑由舊的 Downloads 位置修正為目前工作區。這批變更仍在本機工作樹，下一步是檢查首頁導覽、下載入口與行動版排版，確認後再提交。

**⚠️ 這張表要跟 `aisuni/index.html` 的 `CASES` 陣列保持一致**——2026-07-08 發現兩邊脫鉤過（陣列 10 筆，這裡只列 1 筆），已補齊。之後新增/改案例時兩邊一起改。

## 案例索引

| 案例 | 分類 | 對應專案 | 狀態 | 深度筆記 |
|---|---|---|---|---|
| 手機連動 + Notion 資源整理系統 | 資訊整理 | Notion 工具 + AINewsSuni repo | 完整教材 | [cases/ig-resource-organizer.md](cases/ig-resource-organizer.md) |
| Sona Sheet：多品牌社群貼文半自動化 | 社群自動化 | SonaSNS-Platform | 營運中 | 待寫 |
| AINewsSuni：每日 AI 新聞摘要機器人 | 資料抓取 | AINewsSuni | 營運中 | 待寫 |
| Okiblues 租車：動態定價 + 自動化報表 | 商業營運 | Okiblues（客戶業務） | 營運中 | 待寫 |
| WeatherLab：天氣資料工具 | 資料抓取 | weatherLab | 待寫教材 | — |
| FlightNews：航班資訊工具 | 資料抓取 | FlightNews | 待寫教材 | — |
| InvestUni 投資學堂 | 內容與知識 | InvestUni-LearnHub | 待寫教材 | — |
| MoralJury 道德陪審團短片 | 內容與知識 | MoralJury-Shorts | 待寫教材 | — |
| CapyChill：一支做完的長片躺了 44 天 | 內容與知識 | CapyChill | 完整教材 | [cases/capychill-lofi-channel.md](cases/capychill-lofi-channel.md) |
| PersonalFootage：十年影像資產整理 | 資訊整理 | PersonalFootage | 待寫教材 | — |

## 跟 course-ai-saas（結構化課程）的分工

`course-ai-saas/SYLLABUS.md` 是**讀書順序索引**，不是第三份內容倉庫：
- 課綱裡「對應某個既有/待寫 CASES 專案」的課 → 直接把內容寫進該專案的 `cases/*.md`（順便補齊上面表格的「待寫教材」缺口），SYLLABUS 只放連結
- 課綱裡「跨專案的純概念課」（例如 API Key/OAuth 安全事故、系統健檢與監控）→ 才在 `course-ai-saas/concepts/` 新寫檔案
- 一件事只寫一次：寫 CASES 案例的同時就是在寫課，不是寫兩份

## 結構

```
ai-academy/
├── README.md              ← 本文件，案例索引 + 三套系統分工說明
├── index.html             ← 案例庫網站（單檔，CASES + COLLECT 兩個陣列）
├── cases/                 ← CASES 逐一深度筆記
├── collect-inbox.md       ← COLLECT 候選區（claude-weekly-collect-digest 每週一自動產生，SS 審核）
└── course-ai-saas/        ← 讀書順序索引，內容連回 cases/ 或新寫 concepts/
```
