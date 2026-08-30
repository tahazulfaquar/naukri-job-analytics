import csv
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

# ---------- Load CSV ----------
with open("data/jobs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print("Rows read from CSV:", len(rows))

# Clear previous raw data
cursor.execute("TRUNCATE TABLE raw_jobs;")

for row in rows:
    cursor.execute("""
        INSERT INTO raw_jobs (
            job_id,
            title,
            company,
            rating,
            reviews,
            experience,
            location,
            job_url,
            salary,
            posted,
            skills,
            scraped_at
        )
        VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
    """, (
        row["job_id"] or None,
        row["title"] or None,
        row["company"] or None,
        row["rating"] or None,
        row["reviews"] or None,
        row["experience"] or None,
        row["location"] or None,
        row["job_url"] or None,
        row["salary"] or None,
        row["posted"] or None,
        row["skills"] or None,
        row["scraped_at"] or None
    ))

conn.commit()

print("Raw data loaded successfully.")


# ---------- Transform ----------
with open("sql/transformations.sql", "r", encoding="utf-8") as file:
    transformation_sql = file.read()

cursor.execute(transformation_sql)

conn.commit()

print("Transformation completed successfully.")


# ---------- Close ----------
cursor.close()
conn.close()

print("ETL pipeline completed successfully.")
