# SS 個人資訊生態系架構

**版本**：v1（2026-07-07 與 SS 確認方向）
**用途**：定義「收集 → 整理 → 發佈」整條管線中各專案的分工。改造 FableCase、新增各網站發佈流程時，以本文件為規格書。

## 核心原則：一個大腦，多個出口

- **Notion「IG 收藏整理」是唯一真相來源**（沿用 [CLAUDE.md](CLAUDE.md) 既有規則），所有來源收集到的資源都進這個資料庫。
- 各網站只是**發佈出口**，按分類認領「已整理」的項目，不自己另存一套資料。
- **「待整理」的項目永遠不會被自動發佈**——這是「自動同步但必須整理過」的防線。

```
【輸入層】兩個來源，寫進同一個 Notion
  ├─ SS 主動丟連結 → AINewsSuni session 整理 → Notion（現行流程）
  └─ FableCase 定期上網找 Cases/Skills → 同一個 Notion DB
        └─ 自動抓的一律：狀態=待整理、驗證狀態=待驗證

【整理層】Notion = 唯一真相來源
  └─ 週會 review / SS 確認後 → 狀態改「已整理」

【發佈層】各網站按分類認領「已整理」項目
  ├─ 工具 / Skills / Cases / 教學 → FableCase 網站（資源庫主站）
  ├─ 餐廳、8月釜山等旅遊 → SunFamilyTrip
  ├─ 沖繩相關 → okinews
  └─ 生活類 → sosolsunday
```

## 各專案分工

| 專案 | 角色 | 不做什麼 |
|---|---|---|
| [AINewsSuni](https://github.com/sssunwl/AINewsSuni) | AI 新聞機器人 + SS 隨手丟連結的收集入口 + RESOURCES.md 輕量索引 | 不做資源展示網站 |
| [Fablecase](https://github.com/sssunwl/Fablecase) | 自動上網找資源/Cases/Skills + **工具資源庫網站**（分類展示、可展開詳細、同類比較） | 不自己另存資料，一律寫進 Notion |
| [SunFamilyTrip](https://github.com/sssunwl/SunFamilyTrip) | 家庭旅遊發佈出口（餐廳、8月釜山等） | 不做收集 |
| [okinews](https://github.com/sssunwl/okinews) | 沖繩相關發佈出口 | 不做收集 |
| [sosolsunday](https://github.com/sssunwl/sosolsunday) | 生活類發佈出口 | 不做收集 |

## Notion 資料庫要加的欄位

| 欄位 | 型別 | 選項 | 用途 |
|---|---|---|---|
| 來源 | select | 手動 / FableCase自動 | 區分 SS 丟的與機器找的 |
| 發佈到 | select | FableCase / SunFamilyTrip / okinews / sosolsunday / 不發佈 | 發佈路由；大多可從「分類」自動推，此欄位供手動覆蓋 |

> 欄位由 SS 或 Sun（本機 session）在 Notion 加，雲端 session 不自行新增選項（沿用 CLAUDE.md 規則）。

分類 → 發佈目標的預設對應：

| 分類 | 預設發佈到 |
|---|---|
| Claude Code 教學、線上課程、其他（工具類） | FableCase |
| 餐廳、8月釜山 | SunFamilyTrip |
| 文章/網頁 | 視內容：工具教學 → FableCase，生活 → sosolsunday |
| 沖繩相關（未來可能新增分類） | okinews |

## 同步機制：自動，但必須整理過

排程一個每週的 Claude session（可用 Claude Code 的 Routine / GitHub Actions 觸發）：

1. 只撈 Notion 裡**狀態=已整理**且有發佈目標的項目
2. 清理內容、補「怎麼用」「同類工具比較優缺點」
3. 生成對應網站的資料（JSON / MD）
4. **開 PR 給 SS 審核**，merge 才上線

FableCase 的自動找資源排程則是反方向：上網找 → 寫進 Notion（待整理/待驗證）→ 等週會確認，**不直接上任何網站**。

## 待辦清單（依優先順序）

### Phase 0：資料品質（先做，否則髒資料上網站）
- [ ] 套用 [notion-sync/PENDING_NOTION_UPDATES.md](notion-sync/PENDING_NOTION_UPDATES.md) 的 5 筆亂碼修正到 Notion
- [ ] SS/Sun 在 Notion 加「來源」「發佈到」兩個欄位

### Phase 1：FableCase 改造（資源庫主站）
- [ ] 盤點 FableCase 現況（repo 結構、現有功能）
- [ ] 建資源庫網站：分類導覽＋卡片列表＋展開完整欄位＋同類比較區塊
- [ ] 資料來源：從 Notion「已整理」項目生成的 `data.json`
- [ ] 自動找資源排程：定期搜 Cases/Skills → 寫 Notion（待整理）

### Phase 2：發佈管線
- [ ] 每週同步 session：Notion 已整理 → 各網站資料 → PR
- [ ] SunFamilyTrip 接收餐廳/釜山類（8月釜山行後第一批內容）
- [ ] okinews / sosolsunday 接口視內容量再開

### Phase 3：閉環
- [ ] 週會 checklist 加入：確認暫存區、審發佈 PR、review 待整理
- [ ] 視運行情況調整分類與自動化頻率
