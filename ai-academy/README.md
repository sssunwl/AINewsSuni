# AI 學院

用自己真實在跑的 AI 應用專案當教材，教別人怎麼跟 AI 協作。

**案例庫網站**：[index.html](index.html) — 單一 HTML 檔，瀏覽器直接開。案例卡片＋分類篩選＋搜尋＋協作心法（含可複製指令）。新增案例改檔案裡的 `CASES` 陣列即可。

- **線上版**：<https://sssunwl.github.io/Fablecase/>（repo：[sssunwl/Fablecase](https://github.com/sssunwl/Fablecase)，公開）
- **單一真相來源是這裡的 index.html**，Fablecase repo 只是部署鏡像。更新流程：改這裡 → 複製 `index.html`（和 `cases/`）到 Fablecase repo → commit push，Pages 會自動重建。

**收集箱週報（排程自動化）**：每週一 09:00 排程任務（`claude-weekly-collect-digest`）掃描來源、產最多 5 筆候選寫進 [collect-inbox.md](collect-inbox.md)，**只進候選區、不自動上站**。沒審核的候選留著併入每週 review。狀態：候選 / 已上站 / 略過。

SS 回「上 N」之後，當時的 session 必須**一次做完下面四件事**，不可以只做前兩項——上站跟 Notion 分開做是資料分裂的根源，之前已經因為漏做而被抓到過一次：

1. 把該筆加進本機 `index.html` 的 `COLLECT` 陣列
2. 複製 `index.html` 到 Fablecase repo、commit push（Pages 自動重建）
3. **寫進 Notion「IG 收藏整理」資料庫**（同一個庫，分類選「Claude Code 教學」）——這是所有收集項目的唯一真相來源，網站只是精選公開版，兩邊都要有
4. 把 `collect-inbox.md` 裡該筆的狀態從「候選」改成「已上站」

每個案例對應 `/Users/sws/Downloads/claude` 底下的一個實際專案（例如 AINewsSuni、InvestUni-LearnHub、WeatherLab...），記錄的不只是「做出了什麼」，而是**需求 → 設計討論 → 取捨決策**的完整過程。

## 案例索引

| 案例 | 對應專案 | 重點 |
|---|---|---|
| [IG / 資源整理系統](cases/ig-resource-organizer.md) | (Notion 工具，非本機專案) | 手機連動 Claude Code、訂閱方案取捨、Notion 資料庫設計 |

## 結構

```
ai-academy/
├── README.md          ← 本文件，案例索引
├── index.html         ← 案例庫網站（單檔，可直接開或部署 GitHub Pages）
└── cases/             ← 逐一案例的教學筆記
```
