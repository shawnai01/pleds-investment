#!/usr/bin/env python3
"""
TIMEFOLIO 액티브 ETF 일별 보유종목 수집 + 변화 분석
Data source: investing.com (Top 10 holdings)
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent / "etf-holdings"

ETFS = {
    "456600": {"name": "글로벌AI인공지능", "url": "https://kr.investing.com/etfs/456600-seoul-holdings"},
    "426030": {"name": "미국나스닥100", "url": "https://kr.investing.com/etfs/426030-seoul-holdings"},
    "478150": {"name": "우주테크방산", "url": "https://kr.investing.com/etfs/478150-seoul-holdings"},
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch_holdings(ticker: str, url: str) -> list[dict]:
    """Fetch top holdings from investing.com"""
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    holdings = []
    tables = soup.find_all("table")
    for table in tables:
        header_row = table.find("tr")
        if not header_row:
            continue
        ths = [th.get_text(strip=True) for th in header_row.find_all("th")]
        if "% 비중" not in ths and "% Assets" not in ths:
            continue

        for row in table.find_all("tr")[1:]:
            cells = [td.get_text(strip=True) for td in row.find_all("td")]
            if len(cells) >= 4:
                name = cells[1]
                symbol = cells[2] if cells[2] != "-" else ""
                weight_str = cells[3].replace("%", "").replace(",", "")
                try:
                    weight = float(weight_str)
                except ValueError:
                    continue
                shares_str = cells[-1].replace(",", "") if len(cells) >= 8 else ""
                try:
                    shares = int(shares_str)
                except ValueError:
                    shares = 0
                holdings.append({
                    "name": name,
                    "symbol": symbol,
                    "weight": weight,
                    "shares": shares,
                })
    return holdings


def save_holdings(ticker: str, holdings: list[dict], date_str: str):
    """Save holdings to JSON file"""
    out_dir = BASE_DIR / ticker
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{date_str}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"date": date_str, "ticker": ticker, "holdings": holdings, "collected_at": datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)
    return path


def load_holdings(ticker: str, date_str: str) -> list[dict] | None:
    path = BASE_DIR / ticker / f"{date_str}.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)["holdings"]
    return None


def find_prev_date(ticker: str, current_date: str) -> str | None:
    """Find the most recent previous data file"""
    out_dir = BASE_DIR / ticker
    if not out_dir.exists():
        return None
    files = sorted([f.stem for f in out_dir.glob("*.json") if f.stem < current_date], reverse=True)
    return files[0] if files else None


def compute_diff(prev: list[dict], curr: list[dict]) -> dict:
    """Compute holdings changes between two dates"""
    prev_map = {h["symbol"] or h["name"]: h for h in prev}
    curr_map = {h["symbol"] or h["name"]: h for h in curr}

    added = []
    removed = []
    weight_changes = []

    for key, h in curr_map.items():
        if key not in prev_map:
            added.append(h)
        else:
            delta = h["weight"] - prev_map[key]["weight"]
            if abs(delta) >= 0.05:
                weight_changes.append({
                    "name": h["name"],
                    "symbol": h["symbol"],
                    "prev_weight": prev_map[key]["weight"],
                    "curr_weight": h["weight"],
                    "delta": round(delta, 2),
                    "prev_shares": prev_map[key].get("shares", 0),
                    "curr_shares": h.get("shares", 0),
                })

    for key, h in prev_map.items():
        if key not in curr_map:
            removed.append(h)

    weight_changes.sort(key=lambda x: abs(x["delta"]), reverse=True)
    return {"added": added, "removed": removed, "weight_changes": weight_changes}


def format_report(results: dict, date_str: str) -> str:
    """Generate markdown report"""
    lines = [f"# TIMEFOLIO ETF 일별 변화 리포트 — {date_str}\n"]

    for ticker, info in results.items():
        etf = ETFS[ticker]
        lines.append(f"\n## {etf['name']} ({ticker})\n")

        if not info.get("diff"):
            lines.append("ℹ️ 이전 데이터 없음 (첫 수집)\n")
            lines.append("**현재 Top 10:**\n")
            lines.append("| # | 종목 | 티커 | 비중 | 주수 |")
            lines.append("|---|------|------|------|------|")
            for i, h in enumerate(info["holdings"][:10], 1):
                lines.append(f"| {i} | {h['name']} | {h['symbol']} | {h['weight']:.2f}% | {h['shares']:,} |")
            continue

        diff = info["diff"]
        prev_date = info["prev_date"]
        lines.append(f"비교: {prev_date} → {date_str}\n")

        if diff["added"]:
            lines.append("### 🟢 신규 편입")
            for h in diff["added"]:
                lines.append(f"- **{h['name']}** ({h['symbol']}) — {h['weight']:.2f}%")

        if diff["removed"]:
            lines.append("\n### 🔴 편출")
            for h in diff["removed"]:
                lines.append(f"- ~~{h['name']}~~ ({h['symbol']}) — 이전 {h['weight']:.2f}%")

        if diff["weight_changes"]:
            lines.append("\n### 📊 비중 변화 (|Δ| ≥ 0.05%p)")
            lines.append("| 종목 | 티커 | 이전 | 현재 | 변화 |")
            lines.append("|------|------|------|------|------|")
            for c in diff["weight_changes"]:
                arrow = "🔺" if c["delta"] > 0 else "🔻"
                lines.append(f"| {c['name']} | {c['symbol']} | {c['prev_weight']:.2f}% | {c['curr_weight']:.2f}% | {arrow} {c['delta']:+.2f}%p |")

        if not diff["added"] and not diff["removed"] and not diff["weight_changes"]:
            lines.append("✅ 유의미한 변화 없음\n")

    # Cross-ETF analysis
    all_holdings = {}
    for ticker, info in results.items():
        for h in info["holdings"]:
            key = h["symbol"] or h["name"]
            if key not in all_holdings:
                all_holdings[key] = {"name": h["name"], "symbol": h["symbol"], "etfs": []}
            all_holdings[key]["etfs"].append(ETFS[ticker]["name"])

    overlap = {k: v for k, v in all_holdings.items() if len(v["etfs"]) >= 2}
    if overlap:
        lines.append("\n## 🔗 교차 보유 종목 (2개+ ETF 공통)")
        for key, v in overlap.items():
            lines.append(f"- **{v['name']}** ({v['symbol']}) — {', '.join(v['etfs'])}")

    return "\n".join(lines)


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    results = {}

    for ticker, etf in ETFS.items():
        print(f"Collecting {etf['name']} ({ticker})...")
        try:
            holdings = fetch_holdings(ticker, etf["url"])
            save_holdings(ticker, holdings, today)
            print(f"  ✅ {len(holdings)} holdings saved")

            prev_date = find_prev_date(ticker, today)
            diff = None
            if prev_date:
                prev = load_holdings(ticker, prev_date)
                diff = compute_diff(prev, holdings)
                print(f"  📊 vs {prev_date}: +{len(diff['added'])} -{len(diff['removed'])} Δ{len(diff['weight_changes'])}")

            results[ticker] = {"holdings": holdings, "diff": diff, "prev_date": prev_date}
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results[ticker] = {"holdings": [], "diff": None, "prev_date": None, "error": str(e)}

    report = format_report(results, today)
    report_path = BASE_DIR / f"report-{today}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n📄 Report: {report_path}")
    print(report)


if __name__ == "__main__":
    main()
