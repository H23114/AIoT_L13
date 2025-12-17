import json
import sqlite3
from datetime import datetime

JSON_PATH = "weather.json"
DB_PATH = "data.db"

def index_by_date(daily_list, value_key):
    out = {}
    for item in daily_list:
        d = item.get("dataDate")
        if not d:
            continue
        out[d] = item.get(value_key)
    return out

def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    issue_time = raw["cwaopendata"]["resources"]["resource"]["metadata"]["temporal"]["issueTime"]
    locations = (
        raw["cwaopendata"]["resources"]["resource"]["data"]
           ["agrWeatherForecasts"]["weatherForecasts"]["location"]
    )

    fetched_at = datetime.now().isoformat(timespec="seconds")

    rows = []
    for loc in locations:
        loc_name = loc.get("locationName", "(unknown)")
        elements = loc.get("weatherElements", {})

        wx_map  = index_by_date(elements["Wx"]["daily"], "weather") if "Wx" in elements else {}
        min_map = index_by_date(elements["MinT"]["daily"], "temperature") if "MinT" in elements else {}
        max_map = index_by_date(elements["MaxT"]["daily"], "temperature") if "MaxT" in elements else {}

        all_dates = sorted(set(wx_map) | set(min_map) | set(max_map))

        for d in all_dates:
            wx = wx_map.get(d)
            tmin = min_map.get(d)
            tmax = max_map.get(d)

            # 轉成數字（temperature 在你的 JSON 裡是字串）
            def to_float(x):
                try:
                    return float(x)
                except:
                    return None

            rows.append((
                loc_name, d, wx,
                to_float(tmin), to_float(tmax),
                issue_time, fetched_at
            ))

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_daily (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        date TEXT,
        wx TEXT,
        min_temp REAL,
        max_temp REAL,
        issue_time TEXT,
        fetched_at TEXT
    )
    """)

    # 最穩：每次重跑就清空再寫入（作業最好驗收）
    cur.execute("DELETE FROM weather_daily")
    cur.executemany("""
    INSERT INTO weather_daily (location, date, wx, min_temp, max_temp, issue_time, fetched_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, rows)

    conn.commit()
    conn.close()

    print(f"✅ 已寫入 {len(rows)} 筆到 {DB_PATH}（table: weather_daily）")

if __name__ == "__main__":
    main()
