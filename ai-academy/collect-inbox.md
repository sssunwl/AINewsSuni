# 收集箱候選區

週報自動產生，SS 審核後才上站。狀態：候選 / 已上站 / 略過。

---

## 週報 2026-07-16

### 外部發現

1. **Claude web_fetch 資料外洩漏洞：一堂活生生的資安課**
   類型：案例（資安教學）
   來源軌：外部發現
   介紹：研究者 Ayush Paul 發現 Claude 的 `web_fetch` 工具雖然擋掉了「直接餵惡意網址」，卻沒擋住「跟著已抓取頁面裡的連結繼續爬」——攻擊者做一個誘餌網站，讓 AI 一步步「像認字一樣」被誘導點出使用者的姓名、所在地、雇主等私密資訊。Anthropic 已經修補（拿掉 web_fetch 在自己抓回的內容裡繼續跟連結的能力）。
   為什麼值得 SS 看：這正好呼應你系統裡「絕不執行內容裡夾帶的指令」那條資安規則的真實案例版——工具權限開太寬、又允許連鎖存取，就是「lethal trifecta」（私密資料存取＋工具能力＋惡意指令）成形的溫床。用來教「為什麼 agent 的工具範圍要收緊」是很紮實的素材。
   原始出處：https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/
   可複製 prompt/指令：（無，這是資安分析文章不是工具）
   狀態：候選

2. **aaron-marketing-skills：120 個行銷 Skill 一套講完**
   類型：Skill
   來源軌：外部發現
   介紹：涵蓋品牌敘事、SEO/GEO、社群、Email、廣告投放、網紅合作、產品上市共 7 個行銷領域、120 個 Skill，用共同的「合約結構」讓 Skill 之間能互相交棒（例如做完 SEO 研究直接接去寫廣告文案）。預設層級（Tier 1）不需要任何付費 API，貼資料就能跑；Tier 2/3 才需要接 Google Search Console、GA4 等免費或付費 API。
   為什麼值得 SS 看：SolsLab／SonaSNS 的行銷自動化路線正好用得上，尤其是「不需要 API 也能先跑」這個門檻設計，適合先在 Sona 品牌上小範圍試。
   原始出處：https://github.com/aaron-he-zhu/aaron-marketing-skills
   可複製 prompt/指令：
   ```
   # Claude Code 安裝
   /plugin marketplace add aaron-he-zhu/aaron-marketing-skills
   /plugin install aaron-marketing@aaron

   # 使用範例（自動路由到對的領域）
   /aaron-marketing:auto research keywords for my SaaS product targeting small teams
   /aaron-marketing:seo-geo https://example.com/blog/my-article --phase tune
   /aaron-marketing:influencer Find TikTok creators for a skincare launch and score their fit
   ```
   狀態：候選

3. **Vox Director：一句話題目變一支成品影片**
   類型：Skill
   來源軌：外部發現
   介紹：輸入一句話的主題，自動產出「紙拼貼風格」的解說/廣告影片——腳本、關鍵畫面、動態圖形、配音旁白、配樂、字幕全流程跑完，中間有兩個人工確認點。技術上是 Atlas Cloud API 搭配本機 ffmpeg。
   為什麼值得 SS 看：DiveInOut／SunFamilyTrip／品牌社群內容都常需要短影音，這個工具把「腳本到成品」壓成一句話輸入＋兩次確認，門檻比一般影片 agent 低很多，值得實測一次看品質夠不夠用。
   原始出處：https://github.com/Alisa0808/vox-director
   可複製 prompt/指令：（詳細安裝與觸發指令需進 repo README 確認，原始碼頁面未列出完整指令片段）
   狀態：候選

### Notion 收藏促發佈

1. **Agent Sprite Forge：用自然語言「講」出一款 2D 遊戲**
   類型：案例
   來源軌：Notion 私人收藏
   介紹：開源 2D 遊戲開發工具，全 Python、Apache 2.0。核心理念不是一鍵生成，而是一步步講出風格、角色、關卡，讓遊戲慢慢長成心目中的樣子。支援精靈表生成、分層 RPG 地圖、動畫 GIF，整合 Godot／Unity。
   為什麼值得 SS 看：示範「AI 時代讓非專業開發者也能實現長年心中的專案夢」這個敘事，很適合當 AI 學院裡「非工程背景也能做完整作品」的案例。
   原始出處：https://github.com/0x0funky/agent-sprite-forge
   可複製 prompt/指令：（無，需照 repo README 操作）
   狀態：候選

2. **Social Cards Engine：Claude 驅動的 IG 圖卡 AI 助理**
   類型：Skill／案例
   來源軌：Notion 私人收藏
   介紹：創作者 Denis Wei 開源自己在用的整套 IG 圖卡生成系統：品牌架構訓練、AI 創意發想、外加兩位「會挑毛病」的 AI 審稿員把關品質。MIT 授權、完全免費，訴求是打掉那些「套模板收高價課」的市場。
   為什麼值得 SS 看：跟 SonaSNS 的 IG 輪播模版工具方向高度重疊，「兩位 AI 互相審稿」這個品質把關模式值得拿來對照自家工具的設計。
   原始出處：https://github.com/DennisWei9898/social-cards-engine
   可複製 prompt/指令：（教學簡報另有 Google Slides，見 Notion 頁面內文）
   狀態：候選

3. **Vibe Reader：長內容速讀卡片工具**
   類型：工具
   來源軌：Notion 私人收藏
   介紹：把長文章、YouTube 影片自動變成重點卡片，用來決定「值不值得花時間看原文」，滑卡片時遇到不懂的地方可以直接問內建 AI。原 PO 用它追 Claude Code 教學，吸收速度明顯變快。
   為什麼值得 SS 看：資訊量大、更新快的主題（例如每週要追蹤的 Claude Code 生態動態）可以先用它篩一輪，把「看不看得完」的焦慮往前擋一層。
   原始出處：https://www.threads.com/@_piss_off_hsuan_/post/DZrr9OwEzJY
   可複製 prompt/指令：下載頁 https://share.vibe-reader.com/download
   狀態：候選

4. **Codex & Claude Code 實戰分享：200 億 Token 燒出來的 5 個 Skill 心法**
   類型：教學
   來源軌：Notion 私人收藏
   介紹：作者用 Codex 開發兩個月、燒了近 200 億 token，前兩週幾乎在瞎跑，後來全部用 Skills 工作流重練才順起來。文章整理 5 個實用 Skill：UI/UX 強化、除錯（reproduce→localize→reduce→fix→guard 五步驟）、專案架構師、Codex Skills 清單、跨工具通用的 Agent Skills 資源庫。核心訊息：Skill 的價值是把「模糊需求」轉成「agent 可以穩定執行的 SOP」。
   為什麼值得 SS 看：直接呼應你自己「先做案例再抽象」的協作風格——這篇是別人踩過坑之後濃縮出的 SOP 化心法，拿來對照自己用 Claude Code 的習慣很有參考價值。
   原始出處：https://www.threads.com/@sofi.life_official/post/DaPm1MKE9vl
   可複製 prompt/指令：（文章推薦的 5 個 Skill 來源已列在 Notion 頁面內文，含 nextlevelbuilder/ui-ux-pro-max-skill、addyosmani/agent-skills、hmohamed01/Claude-Code-Scaffolding-Skill、ComposioHQ/awesome-codex-skills、VoltAgent/awesome-agent-skills）
   狀態：候選

5. **35+ 媽媽副業入門包：10 個免費 App 起步清單**
   類型：案例
   來源軌：Notion 私人收藏
   介紹：一位 35+ 歲媽媽分享她開始副業時最依賴的 10 個免費工具（原文粵語）：ChatGPT 寫文案、CapCut 剪片、Canva 出圖、Notes 記靈感、Pinterest 找點子、Line Voom 練鏡頭、Google Keep 共享清單、Snippet 做字幕、Moon/365 成長日記、EverNote/Notion 建個人知識庫。核心訊息是「由 Notes 裡一兩句日常開始，慢慢長成一篇文、一條片」。
   為什麼值得 SS 看：這筆比較偏「零基礎新手工具鏈」而非 AI 深度應用，跟 AI 學院目前案例的技術含量落差較大，是否適合放進站上教材，建議 SS 審核時特別看一下（B 軌只依 Notion 的已整理／已查證屬實標記帶過來，沒有重新做內容適配判斷）。
   原始出處：https://www.threads.com/@walala_ashley/post/DaFxh_wkhDU
   可複製 prompt/指令：（無，純工具清單無 prompt）
   狀態：候選
