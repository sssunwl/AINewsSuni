# AI 學院

用自己真實在跑的 AI 應用專案當教材，教別人怎麼跟 AI 協作。

**案例庫網站**：[index.html](index.html) — 單一 HTML 檔，瀏覽器直接開。案例卡片＋分類篩選＋搜尋＋協作心法（含可複製指令）。新增案例改檔案裡的 `CASES` 陣列即可。

- **線上版**：<https://sssunwl.github.io/Fablecase/>（repo：[sssunwl/Fablecase](https://github.com/sssunwl/Fablecase)，公開）
- **單一真相來源是這裡的 index.html**，Fablecase repo 只是部署鏡像。更新流程：改這裡 → 複製 `index.html`（和 `cases/`）到 Fablecase repo → commit push，Pages 會自動重建。

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
