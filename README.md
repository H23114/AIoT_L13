# AIoT HW3 – Part 1  
Weather Data Crawler, SQLite Storage, and Streamlit Visualization

## 📌 Project Overview
This project processes weather forecast data from the **Central Weather Administration (CWA)**  
dataset **F-A0010-001 (Weekly Agricultural Weather Forecast)**.

The workflow includes:
1. Downloading CWA weather data in JSON format (stored locally)
2. Parsing weather information (Wx, MinT, MaxT)
3. Storing parsed data into an SQLite database
4. Displaying the stored data using a Streamlit web application

---

## 📂 Project Structure
```
AIoT-HW3/
│── crawler.py        # Parse JSON and store data into SQLite
│── app.py            # Streamlit app to display weather data
│── weather.json      # Local CWA JSON data (F-A0010-001)
│── data.db           # SQLite database
│── requirements.txt
│── README.md
```

---

## ⚙️ Environment Setup
Install required Python packages:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```txt
requests
pandas
streamlit
```

---

## ▶️ How to Run

### Step 1: Parse JSON and Store Data into SQLite
```bash
python crawler.py
```
After execution, the SQLite database file `data.db` will be created or updated.

---

### Step 2: Run Streamlit Application
```bash
streamlit run app.py
```
The Streamlit web interface will open in your browser and display weather data stored in `data.db`.

---

## 🗄️ Database Schema
Table name: `weather_daily`

| Column | Type | Description |
|------|------|------------|
| id | INTEGER | Primary key |
| location | TEXT | Region name |
| date | TEXT | Forecast date |
| wx | TEXT | Weather description |
| min_temp | REAL | Minimum temperature |
| max_temp | REAL | Maximum temperature |
| issue_time | TEXT | Forecast issue time |
| fetched_at | TEXT | Data processing timestamp |

---

## 🖥️ Streamlit Output
The Streamlit interface displays:
- Application title and description
- Weather forecast data loaded from the SQLite database
- Tabular view of daily weather information for each region

*(Screenshot of the Streamlit interface is included in the homework submission.)*

---

## 📎 Data Source
- Central Weather Administration (CWA)
- Dataset ID: **F-A0010-001**
- Weekly Agricultural Weather Forecast

---

## ✅ Assignment Requirements Checklist
- JSON data parsing ✔  
- SQLite database creation and insertion ✔  
- Python-based data processing ✔  
- Streamlit data visualization ✔  
