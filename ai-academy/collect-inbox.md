# 收集箱候選區

週報自動產生，SS 審核後才上站。狀態：候選 / 已上站 / 略過。

---

## 週報 2026-07-20

### 外部發現

1. **BaoCut：用自然語言操控影片剪輯的 Claude Code Skill**
   類型：Skill
   來源軌：外部發現
   介紹：開源 Agent Skill，讓 Claude Code／Codex 這類 AI agent 直接對 macOS App「BaoCut」下自然語言指令，完成轉錄逐字稿、字幕生成與翻譯、講者辨識、剪輯等影片處理工作。App 本體（baocut.app）需另外安裝，這個 Skill 只是讓 AI 能操控它的 CLI。
   為什麼值得 SS 看：SunFamilyTrip／DiveInOut／IG 內容都常需要影片後製，這個 Skill 把「打字下指令→自動剪片」的門檻壓到最低，適合實測能不能取代部分手動剪輯流程。
   原始出處：https://github.com/JimLiu/baocut
   可複製 prompt/指令：
   ```
   npx skills add JimLiu/baocut -g -a claude-code codex -y
   ```
   安裝後直接用自然語言下指令，例如：「Transcribe and translate talk.mp4 to Chinese」，或輸入 /baocut
   狀態：候選

2. **natural-japanese：日文商業文件去除「AI 臭」的 Claude Skill**
   類型：Skill
   來源軌：外部發現
   介紹：專門修飾日文商業文件（議事錄、報告、內部指南、研究筆記、簡報大綱）的 Agent Skill，用「寫作前先設計、生成中加約束、生成後機械檢測」三層防線去除 AI 腔調。機械檢測用 sudachipy 做形態素解析找出「AI 味」的用詞與句型，但最終要不要改交給人判斷。
   為什麼值得 SS 看：直接對應 SS 自己「禁 AI 腔」的文案風格規範，而且是日文版——沖繩事業（Okiblues 等）如果要出日文對外文件，這個工具可以拿來把關，跟英文版的 LLM Cliché Highlighter（本週外部發現第 5 筆）剛好湊成中英日對照案例組。
   原始出處：https://github.com/coji/natural-japanese
   可複製 prompt/指令：
   ```
   npx skills add coji/natural-japanese
   ```
   安裝後：`/natural-japanese score <檔名>` 可只評分不修改；或直接請 Claude 照這個 Skill 的規則寫／潤日文文件（需要 uv 執行 Python 檢測腳本）。
   狀態：候選

3. **mentor：幫你分析「自己怎麼用 AI」的 Claude Code 使用報告 Skill**
   類型：Skill
   來源軌：外部發現
   介紹：讀取本機 Claude Code／Codex 的對話紀錄，自動產出一份 8 個章節的 HTML 報告：你都在做什麼專案、哪裡最浪費時間、哪些功能沒用到、可以怎麼調整 CLAUDE.md 減少重複踩坑。全程本機執行，不上傳任何資料。
   為什麼值得 SS 看：SS 自己天天跨多個專案用 Claude Code（sun-agents、AIoffice、SnowS 等），這種「回顧自己怎麼用 AI」的報告拿來做每月自我檢討、或當 AI 學院示範「AI 能自我診斷使用習慣」的教材都很合適。
   原始出處：https://github.com/smixs/mentor
   可複製 prompt/指令：
   ```
   npx skills add smixs/mentor
   ```
   安裝後輸入 `/mentor`（預設分析近 30 天），或 `/mentor --days 60` 自訂區間；報告輸出在 `~/.claude/usage-data/mentor-report.html`
   狀態：候選

4. **equity-research-skill：一句話生成機構級個股投研報告的 Skill**
   類型：Skill
   來源軌：外部發現
   介紹：只要說「研究一下 NVDA」或「AMD 現在貴不貴」，就會照九章結構（業務、競爭優勢、管理層、財務、跨方法估值交叉驗證、分析師共識、催化劑、投資結論）產出中文投研報告，估值用 DCF／EPV／相對估值等至少三種方法交叉驗證，且所有計算都跑 Python 腳本而非純靠語言模型心算。支援美股／港股／A 股，含 A/H 股溢價比較。
   為什麼值得 SS 看：直接對應 SS 本人美港台股＋加密貨幣的投資習慣、重視比價與成本效益的偏好，也可以評估要不要把這套邏輯簡化後放進 InvestUniS 投資學堂當教學案例。
   原始出處：https://github.com/rollingSirius/equity-research-skill
   可複製 prompt/指令：
   ```
   git clone https://github.com/rollingSirius/equity-research-skill.git ~/.claude/skills/equity-research
   ```
   安裝後直接用自然語言問，例如：「研究一下 NVDA」
   狀態：候選

5. **LLM Cliché Highlighter：一鍵抓出 AI 腔英文的網頁小工具**
   類型：工具
   來源軌：外部發現
   介紹：Simon Willison 做的免安裝網頁工具，貼上文字或網址，即時把「一看就是 AI 寫的」老套用語（例如常見的「no X, no Y」句型）標記出來，滑鼠移過去還會顯示是哪個「AI 腔」模式命中的。也提供給工程師用的 Node.js 無頭版本可以跑自動化測試。
   為什麼值得 SS 看：跟 natural-japanese（本週外部發現第 2 筆）剛好是英文版對照組，可以直接拿來把關 AI 學院／SonaSNS／客戶 Portal 的英文文案，驗證「禁 AI 腔」規則有沒有真的落實，不用等人工肉眼抓。
   原始出處：https://tools.simonwillison.net/llm-cliche-highlighter
   可複製 prompt/指令：無需安裝，開網頁貼文字即可用：https://tools.simonwillison.net/llm-cliche-highlighter
   狀態：候選

### Notion 收藏促發佈

（以下 9 筆為本週新符合條件的項目；另有 5 筆——Agent Sprite Forge、Social Cards Engine、Vibe Reader、Codex & Claude Code 實戰分享、35+ 媽媽副業入門包——已在上週 2026-07-16 候選清單出現過且尚未有 SS 決定，本週不重複列出，仍留在上週區塊等待 review。）

1. **【AI教學】用 Claude 一鍵生成 7 篇 IG 輪播貼文（1080x1440）**
   類型：教學／案例
   來源軌：Notion 私人收藏
   介紹：用一句 prompt「請幫我生成7篇IG輪播貼文,大小要是1080X1440」直接讓 Claude 產出整組輪播圖，完整 30 分鐘教學需私訊作者索取，公開內容僅為成果展示。
   為什麼值得 SS 看：跟 SonaSNS／IG 輪播模版工具方向直接重疊，可以測試「純文字 prompt 出輪播圖」這條路線是否比現有工具更省事。
   原始出處：https://www.instagram.com/reel/DZpcymoSd52/
   可複製 prompt/指令：「請幫我生成7篇IG輪播貼文,大小要是1080X1440」（僅此一句公開，完整教學需向原作者私訊索取）
   狀態：候選

2. **【Claude Skill】一人自媒體養 6 個 AI 顧問團（多角色 Skill 內部先開會再回答）**
   類型：Skill／案例
   來源軌：Notion 私人收藏
   介紹：用 Claude Skill 設定 6 個不同角色的 AI 工作人員，先讓他們「內部開會討論」再產出最終答案，作者實測比直接問一個 AI 品質更高，定位為一人公司的決策疲勞解方。具體 Skill 設定步驟未公開，需私訊索取。
   為什麼值得 SS 看：直接對應 Sol/Sun 的多 agent 分工設計，「內部先辯論再定案」這個機制可以拿來對照 Sol 現有的決策流程。
   原始出處：https://www.instagram.com/p/Dahlh4GEw-o/
   可複製 prompt/指令：（未公開，需私訊作者索取）
   狀態：候選

3. **【開源工具】claude-real-video：讓 AI 真正看懂影片的關鍵幀抽取工具**
   類型：工具
   來源軌：Notion 私人收藏
   介紹：開源小工具（MIT 授權，已上架 PyPI），解決「ChatGPT 只讀字幕、Claude 不吃影片檔、Gemini 固定間隔抽幀會漏鏡頭」的問題：只抓「畫面真的變了」的關鍵幀去重，再把字幕／聲音整理成逐字稿，本機跑不用上雲端。
   為什麼值得 SS 看：AINewsSuni／內容分析工作流可以拿來測試，尤其適合拆解對手的短影音鉤子。
   原始出處：https://www.instagram.com/p/DaVHoW5CC21/
   可複製 prompt/指令：pip 套件名 claude-real-video，可直接 `pip install claude-real-video` 嘗試；作者完整安裝連結需私訊索取。
   狀態：候選

4. **【Claude】官方 Connector 串接 Adobe 全套（Lightroom/PS/Express/Premiere）**
   類型：工具
   來源軌：Notion 私人收藏
   介紹：Claude 官方正式功能（非第三方外掛），用自然語言直接操控 Lightroom、Photoshop、Express、Premiere，可自動修圖／去背／批量調色／剪輯。條件：Claude Pro 訂閱＋Adobe 帳號，Claude.ai → Connectors 設定即可用。
   為什麼值得 SS 看：攝影／旅遊內容產製（SunFamilyTrip、DiveInOut 素材後製）如果常跑 Adobe，這條官方 connector 路線比找第三方外掛更穩。
   原始出處：https://www.instagram.com/reel/DYRytA9APam/
   可複製 prompt/指令：無需指令，Claude.ai → Connectors → 連結 Adobe 帳號即可啟用。
   狀態：候選

5. **【Claude Code 工具】claude-mem：Claude Code 專用持久記憶壓縮系統**
   類型：工具
   來源軌：Notion 私人收藏
   介紹：GitHub 開源（Apache-2.0），標記為 GitHub Trending 當日第一名，定位是「Claude Code 專用的持久記憶壓縮系統」。
   為什麼值得 SS 看：直接對照 sun-agents/memory 現有的記憶系統設計，尤其「壓縮」機制值得參考，看能不能截長補短。
   原始出處：https://www.instagram.com/reel/DaacxWXj0Xz/
   可複製 prompt/指令：（原文未附完整安裝指令，需自行搜尋 GitHub「claude-mem」確認）
   狀態：候選

6. **【Claude 工作流】Fable 5 規劃＋開工單給 Opus 4.8 執行，一人公司自動化**
   類型：教學／案例
   來源軌：Notion 私人收藏
   介紹：作者把幾十個對話紀錄＋筆記庫煉成 2 個 Claude Skill（自動產輪播、自動剪片），每次用完自動更新經驗；策略上用 Fable 5 做規劃、開工單交給 Opus 4.8 執行以省額度，5 間一人公司靠這套做到 80-90% 工作 AI 代勞。
   為什麼值得 SS 看：正好對應目前「規劃用 Fable、執行用 Opus」的多模型分工策略，可以直接拿來驗證／優化 Sol 跟 Sun 現有的分工方式。
   原始出處：https://www.instagram.com/reel/DagrtjNSxHe/
   可複製 prompt/指令：（完整「五步驟」教學需私訊作者索取「省時」關鍵字）
   狀態：候選

7. **【Claude Code 架構】一個人養出一支 Claude Code 團隊：6 大團隊×子 Skill 完整藍圖**
   類型：案例
   來源軌：Notion 私人收藏
   介紹：作者用 Claude Code 組出 6 個虛擬團隊、共 107 項 Skill 的公司架構：社群、SEO、內容製造、Ads、工程（含 connect-whatsapp-cloud-api）、業務。SS 本人 IG 已私訊索取過完整教學。
   為什麼值得 SS 看：connect-whatsapp-cloud-api 這個 Skill 直接對應現有 Sophia 的 WhatsApp 整合，整體六團隊架構對 Sol/Sun 的多 agent 分工設計極有參考價值，SS 已經拿到教學可直接消化。
   原始出處：https://www.instagram.com/p/DaiFAwHEvQV/
   可複製 prompt/指令：（SS 本人已私訊作者索取完整教學，可從自己收件匣取用）
   狀態：候選

8. **【Claude Design】不會 Figma/PS 也能用 Claude 一句話做輪播/海報/Landing Page**
   類型：教學
   來源軌：Notion 私人收藏
   介紹：作者不懂 Figma，靠 Claude 一句話指令搞定輪播、海報、Landing Page、客戶 deck，論點是「設計不再是技能是品味」——看圖分析風格、直接寫 HTML/CSS 出可 render 的設計稿、用「想要的 vibe」選色排版。
   為什麼值得 SS 看：呼應 SonaSNS 品牌視覺／客戶 Portal 的設計產出流程，尤其「用形容詞而非工具技能做設計」這個切角適合當 AI 學院教材。
   原始出處：https://www.instagram.com/reel/DXrC4RoE_cS/
   可複製 prompt/指令：（完整 18 分鐘拆解教學需私訊作者索取「Claude」關鍵字）
   狀態：候選

9. **【Claude Code Skill】/watch 指令：2 分鐘看完 45 分鐘 YouTube 演講（含圖表數據）**
   類型：Skill
   來源軌：Notion 私人收藏
   介紹：免費 GitHub Claude Code Skill，打 /watch 指令，機制是每隔幾秒截圖連圖表數據一起讀，不只讀逐字稿。45 分鐘演講兩分鐘看完，5 小時影片轉逐字稿成本約 39 美分。SS 本人 IG 已私訊索取過完整安裝教學＋Prompt 包。
   為什麼值得 SS 看：跟 claude-real-video（本週 Notion 收藏第 3 筆）是同一類「讓 AI 真正看懂影片」的方法，且 SS 已經拿到教學可直接測試導入內容分析工作流。
   原始出處：https://www.instagram.com/p/Dah6VsLiew2/
   可複製 prompt/指令：（SS 本人已私訊作者索取完整安裝教學＋Prompt 包，可從自己收件匣取用）
   狀態：候選

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
