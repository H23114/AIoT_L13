import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "data.db"

st.set_page_config(page_title="Weather SQLite Viewer", layout="wide")
st.title("🌦️ Weather Data (SQLite: data.db)")
st.caption("資料來源：CWA F-A0010-001（一週農業氣象預報）")

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM weather_daily ORDER BY location, date", conn)
conn.close()

st.write(f"共 {len(df)} 筆")
st.dataframe(df, use_container_width=True)

# 小加分：篩選
locations = ["全部"] + sorted(df["location"].unique().tolist())
pick = st.selectbox("選擇地區", locations)
if pick != "全部":
    st.dataframe(df[df["location"] == pick], use_container_width=True)
