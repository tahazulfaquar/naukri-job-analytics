# 📊 Naukri Job Analytics

An end-to-end data engineering project that scrapes job listings from Naukri.com, stores them in PostgreSQL, and enables SQL-based job market analysis.

## 🛠️ Tech Stack

* **Python & Selenium** — Web scraping and data extraction
* **CSV** — Intermediate data storage
* **PostgreSQL** — Data storage and querying
* **Docker Compose** — Database containerization
* **SQL** — Job market analysis

## 🏗️ Pipeline Architecture

```text
Naukri.com
    ↓
Python + Selenium
    ↓
CSV Data
    ↓
PostgreSQL (Docker)
    ↓
SQL Analytics
```

## ✨ Features

* Extracts job titles, company names, ratings, experience, locations, and job URLs.
* Collects additional details such as salary and skills where available.
* Exports scraped data to CSV.
* Loads job records into PostgreSQL for querying and analysis.

## 🚀 Getting Started

```bash
git clone https://github.com/tahazulfaquar/naukri-job-analytics.git
cd naukri-job-analytics

python3 -m venv .venv
source .venv/bin/activate

pip install selenium webdriver-manager pyotp psycopg2-binary python-dotenv

cp .env.example .env
```

Configure your database credentials in `.env`, then start PostgreSQL:

```bash
docker compose up -d
```

Run the scraper and loader:

```bash
python main.py
python load.py
```

Ensure the CSV output path matches the input path expected by `load.py`.

## 📈 Analytics Opportunities

* Most in-demand job roles and skills
* Hiring trends by company and location
* Salary distribution across roles
* Experience requirements across job listings

## 🔮 Future Improvements

* Automated orchestration with Apache Airflow
* Data validation and deduplication
* Snowflake integration
* Power BI dashboard

## 👨‍💻 Author

**Taha Zulfaquar** · [GitHub](https://github.com/tahazulfaquar)

---

*Built to transform job listings into structured data and actionable insights.*
