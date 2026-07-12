#!/usr/bin/env python3
"""
Steve's Daily AI Brief
每天 09:00 HKT：更新 docs/data.json（網站）+ 推送 Telegram
"""

import feedparser
import requests
import json
import os
import re
import html as html_lib
import calendar
import time
from datetime import datetime, timezone, timedelta

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "446653315")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

HKT = timezone(timedelta(hours=8))
NOW_HKT = datetime.now(HKT)
CUTOFF_UTC = datetime.now(timezone.utc) - timedelta(hours=28)
WEEKDAYS_ZH = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]

# 輸出路徑（相對於 repo 根目錄，Actions 從根目錄執行）
DATA_JSON = os.path.join("docs", "data.json")

NEWS_FEEDS = [
    ("The Verge",   "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
    ("TechCrunch",  "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/"),
    ("MIT Tech",    "https://www.technologyreview.com/feed/"),
]
TOOLS_PH_URL = "https://www.producthunt.com/feed"
TOOLS_GN_URL = "https://news.google.com/rss/search?q=new+AI+tool+launch&hl=en-US&gl=US&ceid=US:en"

AI_TOOL_KW   = ["ai","gpt","llm","automation","generative","copilot","claude",
                 "assistant","chatbot","machine learning","artificial intelligence","diffusion"]
MAJOR_AI_KW  = ["openai","anthropic","google gemini","google deepmind","meta llama",
                 "mistral","grok","xai","deepseek","nvidia ai","apple intelligence",
                 "claude","chatgpt","gemini","llama"]
SUNIVERSE_KW = ["video","content creator","social media","instagram","tiktok","youtube",
                 "travel","image","photo","writing","copywriting","marketing",
                 "design","aroma","wellness","short-form","reels"]

# ── 工具函數 ──────────────────────────────────────────────────────────
def strip_tags(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = html_lib.unescape(text)
    return re.sub(r"\s+", " ", text).strip()

def esc(text):
    return (text.replace("&","&amp;").replace("<","&lt;")
                .replace(">","&gt;").replace('"',"&quot;"))

def truncate(text, n=120):
    return text[:n] + "…" if len(text) > n else text

def get_pub_date(entry):
    for field in ("published_parsed","updated_parsed"):
        parsed = getattr(entry, field, None)
        if parsed:
            return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
    return None

# ── 翻譯 ─────────────────────────────────────────────────────────────
_cache = {}
_NAME_FIXES = {
    "克勞德":"Claude",
    "法布爾":"Fable","寓言 5":"Fable 5","寓言5":"Fable 5","寓言":"Fable",
    "開放人工智慧":"OpenAI","開放AI":"OpenAI",
    "聊天GPT":"ChatGPT","聊天 GPT":"ChatGPT",
    "雙子座":"Gemini","美達":"Meta","格羅克":"Grok",
    "深度求索":"DeepSeek","米斯特拉爾":"Mistral",
    "拉馬":"Llama","美洲駝":"Llama","安索比克":"Anthropic",
    "科裂":"Cohere","科普洛特":"Copilot","GitHub 副駕駛":"GitHub Copilot",
}
def _fix(text):
    for wrong, right in _NAME_FIXES.items():
        text = text.replace(wrong, right)
    return re.sub(r"([A-Za-z0-9])·([A-Za-z0-9])", r"\1 \2", text)

def translate(text, delay=0.15):
    if not text: return text
    if text in _cache: return _cache[text]
    try:
        time.sleep(delay)
        r = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={"client":"gtx","sl":"en","tl":"zh-TW","dt":"t","q":text},
            timeout=8,
        )
        result = "".join(seg[0] for seg in r.json()[0] if seg[0])
        result = _fix(result)
        _cache[text] = result
        return result
    except Exception:
        return text

def translate_items(news, tools):
    print("Translating…")
    for item in news:
        item["title"]   = translate(item["title"])
        item["summary"] = translate(item["summary"])
    for item in tools:
        item["title_en"] = item["title"]          # 保留英文原名
        zh = translate(item["title"])
        item["title"] = f"{zh} ({item['title_en']})" if zh != item["title_en"] else zh
        item["desc"]  = translate(item.get("desc",""))
    print("  done")

# ── 抓新聞 ────────────────────────────────────────────────────────────
def fetch_news(max_total=8):
    seen, items = set(), []
    for source, url in NEWS_FEEDS:
        if len(items) >= max_total: break
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                if len(items) >= max_total: break
                pub = get_pub_date(entry)
                if pub and pub < CUTOFF_UTC: continue
                title   = (entry.get("title") or "").strip()
                link    = (entry.get("link") or "").strip()
                summary = truncate(strip_tags(entry.get("summary") or entry.get("description") or ""))
                key     = title.lower()[:60]
                if not title or not link or key in seen: continue
                seen.add(key)
                items.append({"title":title,"link":link,"summary":summary,"source":source})
        except Exception as e:
            print(f"[WARN] {source}: {e}")
    return items

# ── 抓工具 ────────────────────────────────────────────────────────────
def fetch_tools(max_items=5):
    seen, items = set(), []
    try:
        feed = feedparser.parse(TOOLS_PH_URL)
        for entry in feed.entries[:40]:
            if len(items) >= max_items: break
            combined = (entry.get("title","")+" "+strip_tags(entry.get("summary") or entry.get("description") or "")).lower()
            if not any(k in combined for k in AI_TOOL_KW): continue
            title = (entry.get("title") or "").strip()
            link  = (entry.get("link") or "").strip()
            desc  = truncate(strip_tags(entry.get("summary") or entry.get("description") or ""), 100)
            key   = title.lower()[:50]
            if title and link and key not in seen:
                seen.add(key)
                items.append({"title":title,"link":link,"desc":desc})
    except Exception as e:
        print(f"[WARN] Product Hunt: {e}")
    if len(items) < 3:
        try:
            feed = feedparser.parse(TOOLS_GN_URL)
            for entry in feed.entries[:10]:
                if len(items) >= max_items: break
                title = (entry.get("title") or "").strip()
                link  = (entry.get("link") or "").strip()
                desc  = truncate(strip_tags(entry.get("summary") or ""), 100)
                key   = title.lower()[:50]
                if title and link and key not in seen:
                    seen.add(key)
                    items.append({"title":title,"link":link,"desc":desc})
        except Exception as e:
            print(f"[WARN] GNews tools: {e}")
    return items[:max_items]

# ── 過濾 ──────────────────────────────────────────────────────────────
def filter_major(news):
    return [i for i in news if any(k in (i["title"]+i["summary"]).lower() for k in MAJOR_AI_KW)][:3]

def filter_suniverse(news, tools):
    sn = [i for i in news  if any(k in (i["title"]+i["summary"]).lower()      for k in SUNIVERSE_KW)][:2]
    st = [i for i in tools if any(k in (i["title"]+i.get("desc","")).lower()   for k in SUNIVERSE_KW)][:2]
    return sn, st

def generate_steve_ideas(news, tools):
    if not GROQ_API_KEY:
        print("  GROQ_API_KEY not set, skipping ideas")
        return []
    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)

        news_lines = "\n".join(f"- {n['title']}" for n in news[:6])
        tool_lines = "\n".join(f"- {t['title']}: {t.get('desc','')}" for t in tools[:4])

        prompt = f"""你是 Steve，Suniverse 的 AI 技術長。說話像個在矽谷工作過的香港人——直接、有點酷、不廢話。你老闆 SS 是旅遊美食內容創作者兼品牌創辦人。

你要給 SS 推薦 3 個這週就能試的 AI 賺錢機會。

工具使用規則（最重要）：
- 每個機會必須以「今日新 AI 工具」清單裡的工具為主角，直接用它來設計機會
- 清單裡沒有合適工具時，才可以用你確定存在的知名工具（CapCut、Runway、ElevenLabs、Kling AI、ChatGPT、Claude、Canva、HeyGen、Midjourney、Descript、Pika）
- 絕對不能自己發明工具名稱

寫作規則（必須遵守）：
1. 標題要像週刊封面標題，不是課本目錄（例如：「用 CapCut AI 10 分鐘出旅遊 Reel」）
2. detail 要像你在 WhatsApp 傳訊息給 SS，說話自然，有具體步驟
3. 每個機會要說清楚：做什麼 → 發在哪 → 預計多久出成果
4. 禁用詞：「在當今」「隨著AI發展」「不妨嘗試」「大幅提升」「值得關注」「可以考慮」「顯著」「賦能」

今日 AI 新聞：
{news_lines}

今日新 AI 工具：
{tool_lines}

只輸出 JSON array，不要 markdown code block，不要其他文字：
[
  {{"title": "標題（15字以內）", "detail": "2-3句，說人話，有具體工具或步驟"}},
  {{"title": "...", "detail": "..."}},
  {{"title": "...", "detail": "..."}}
]"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.85,
            max_tokens=700,
        )
        text = response.choices[0].message.content.strip()
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        ideas = json.loads(text)
        print(f"  {len(ideas)} ideas generated (Groq)")
        return ideas[:3]
    except Exception as e:
        print(f"[WARN] generate_steve_ideas: {e}")
        return []

def steve_pick(news, exclude=None):
    exclude = exclude or set()
    cands = [i for i in news if i["title"] not in exclude]
    for i in cands:
        if any(k in (i["title"]+i["summary"]).lower() for k in MAJOR_AI_KW): return i
    return cands[0] if cands else None

# ── 寫入 data.json ────────────────────────────────────────────────────
def write_data_json(news, tools, sun_news, sun_tools, major, pick, ideas=None):
    # Load existing history to preserve calendar data
    history = {}
    if os.path.exists(DATA_JSON):
        try:
            with open(DATA_JSON, "r", encoding="utf-8") as f:
                existing = json.load(f)
            history = existing.get("history", {})
        except Exception:
            pass

    ideas = ideas or []
    today_key = NOW_HKT.strftime("%Y-%m-%d")
    history[today_key] = {
        "news":          news,
        "tools":         tools,
        "suniverse_news":  sun_news,
        "suniverse_tools": sun_tools,
        "major":       major,
        "pick":        pick,
        "steve_ideas": ideas,
    }

    data = {
        "updated": NOW_HKT.strftime("%Y-%m-%d %H:%M HKT"),
        "news":          news,
        "tools":         tools,
        "suniverse_news":  sun_news,
        "suniverse_tools": sun_tools,
        "major":       major,
        "pick":        pick,
        "steve_ideas": ideas,
        "history":     history,
    }
    os.makedirs("docs", exist_ok=True)
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {DATA_JSON}")

# ── 組 TG 訊息 ────────────────────────────────────────────────────────
def build_tg(news, tools, sun_news, sun_tools, major, pick, ideas=None):
    today   = NOW_HKT.strftime("%Y-%m-%d")
    weekday = WEEKDAYS_ZH[NOW_HKT.weekday()]
    lines = [
        "🤖 <b>Steve's Daily AI Brief</b>",
        f"<i>{today} {weekday}</i>","",
        "🔥 <b>今日 AI 熱聞</b>","",
    ]
    if news:
        for i,item in enumerate(news[:5],1):
            lines.append(f'{i}. <a href="{item["link"]}">{esc(item["title"])}</a>')
            if item.get("summary"): lines.append(f'   <i>{esc(item["summary"])}</i>')
            lines.append("")
    else:
        lines += ["<i>今日暫無新聞</i>",""]

    lines += ["🛠️ <b>新 AI 工具</b>",""]
    if tools:
        for item in tools[:4]:
            lines.append(f'• <a href="{item["link"]}">{esc(item["title"])}</a>')
            if item.get("desc"): lines.append(f'  <i>{esc(item["desc"])}</i>')
            lines.append("")
    else:
        lines += ["<i>今日無新工具</i>",""]

    if sun_news or sun_tools:
        lines += ["🚩 <b>Suniverse 應用機會</b>",""]
        for item in sun_news:
            lines.append(f'🚩 <a href="{item["link"]}">{esc(item["title"])}</a>')
            if item.get("summary"): lines.append(f'   <i>{esc(item["summary"])}</i>')
            lines.append("")
        for item in sun_tools:
            lines.append(f'🚩 <a href="{item["link"]}">{esc(item["title"])}</a>')
            if item.get("desc"): lines.append(f'   <i>{esc(item["desc"])}</i>')
            lines.append("")

    if major:
        lines += ["📊 <b>大廠動態</b>",""]
        for item in major:
            lines.append(f'• <a href="{item["link"]}">{esc(item["title"])}</a>')
            lines.append("")

    if pick:
        lines += [
            "💡 <b>Steve 精選</b>","",
            f'<a href="{pick["link"]}">{esc(pick["title"])}</a>',
            f'<i>{esc(pick["summary"])}</i>' if pick.get("summary") else "","",
        ]

    if ideas:
        lines += ["💰 <b>Steve 今日 3 個賺錢機會</b>",""]
        for i, idea in enumerate(ideas[:3]):
            num = ["1️⃣","2️⃣","3️⃣"][i]
            lines.append(f'{num} <b>{esc(idea["title"])}</b>')
            lines.append(esc(idea["detail"]))
            lines.append("")

    lines += [f'🌐 <a href="https://sssunwl.github.io/AINewsSuni/">AINewsSuni</a>'
              f'  ·  <a href="https://sssunwl.github.io/AIofficeSuni/">Suniverse</a>']

    text = "\n".join(lines)
    if len(text) > 4000:
        text = text[:3970] + "\n…\n\n🌐 <a href=\"https://sssunwl.github.io/AINewsSuni/\">AINewsSuni</a>"
    return text

# ── 發送 ─────────────────────────────────────────────────────────────
def send_telegram(text):
    try:  # 同時鏡射到 Discord #n-ainews(失敗不影響 TG)
        from _discord import notify_discord
        notify_discord(text)
    except Exception:
        pass
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": CHAT_ID, "text": text,
        "parse_mode": "HTML", "disable_web_page_preview": True,
    }, timeout=15)
    resp.raise_for_status()
    return resp.json()

# ── Main ──────────────────────────────────────────────────────────────
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN 未設定")

    print("Fetching news…")
    news = fetch_news()
    print(f"  {len(news)} items")

    print("Fetching tools…")
    tools = fetch_tools()
    print(f"  {len(tools)} items")

    translate_items(news, tools)

    sun_news, sun_tools = filter_suniverse(news, tools)
    major = filter_major(news)
    pick  = steve_pick(news, exclude={i["title"] for i in sun_news})

    print("Generating Steve's ideas…")
    ideas = generate_steve_ideas(news, tools)

    write_data_json(news, tools, sun_news, sun_tools, major, pick, ideas)

    msg = build_tg(news, tools, sun_news, sun_tools, major, pick, ideas)
    print(f"Message {len(msg)} chars")
    result = send_telegram(msg)
    print(f"Sent: {result.get('ok')}")

if __name__ == "__main__":
    main()
