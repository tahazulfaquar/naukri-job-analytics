from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import os
import pyotp
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
naukri_web = "https://www.naukri.com/"
download_dir = r"/mnt/data/Code/jobScraper/downloads"


# ---------- Configuration ----------
def conf(website, download_dir):
    try:
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir
        })
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.get(website)
        print("Configuration successful.")
        return driver
    except Exception as e:
        print(f"Error in configuration: {str(e)}")
        return None


# ---------- Search ----------
def search():
    try:
        # search_txt = input("Enter Skills/ Designations/ Companies- ")
        search_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input")
        search_field.send_keys("data science")
        search_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[6]").click()
        print("Search successful.")
    except Exception as e:
        print(f"Search Failed: {e}")


# ---------- Helper ----------
def get_text(parent, selector):
    try:
        return parent.find_element(By.CSS_SELECTOR, selector).text.strip()
    except:
        return None


# ---------- Scrape details from each card ----------
def scrape_job_details(jobs):
    for job in jobs:
        driver.get(job["job_url"])
        try:
            salary = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_jhc__salary__jdfEC")))
            job["salary"] = salary.text.strip()
        except Exception:
            job["salary"] = None
            print(f"Salary not found: {job['job_url']}")

        try:
            posted = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_jhc__stat__PgY67")))
            job["posted"] = posted.text.strip()
        except Exception:
            job["posted"] = None
            print(f"Posted date not found: {job['job_url']}")

        try:
            skill_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".styles_chip__7YCfG.styles_clickable__dUW8S")))
            skills = [
                skill.text.strip()
                for skill in skill_elements
                if skill.text.strip()
            ]
        except Exception:
            skills = []
            print(f"Skills not found: {job['job_url']}")
        job["skills"] = skills
        job["skills"] = ", ".join(job["skills"])


# ---------- Scrape all cards ----------
def job_card():
    job_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.srp-jobtuple-wrapper")))
    jobs = []
    for card in job_cards:
        company = get_text(card, "a.comp-name")
        rating = get_text(card, "a.rating")
        reviews = get_text(card, "a.review")

        job_url = card.find_element(By.CSS_SELECTOR,"a.title").get_attribute("href")

        job = {
            "job_id": card.get_attribute("data-job-id"),
            "title": get_text(card, "a.title"),
            "company": company,
            "rating": rating,
            "reviews": reviews,
            "experience": get_text(card,"span.exp-wrap"),
            "location": get_text(card,"span.loc-wrap.ver-line"),
            "job_url": job_url,
            "scraped_at": datetime.now().isoformat()
        }
        jobs.append(job)
    return jobs


# ---------- Save Data ----------
def save_jobs(jobs):
    with open("/mnt/data/Code/jobScraper/downloads/jobs.csv","w",newline="",encoding="utf-8") as file:
        fieldnames = [
            "job_id",
            "title",
            "company",
            "rating",
            "reviews",
            "experience",
            "location",
            "job_url",
            "salary",
            "posted",
            "skills",
            "scraped_at"
        ]
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(jobs)
    print(f"Saved {len(jobs)} jobs to jobs.csv")



driver = conf(naukri_web, download_dir)
wait = WebDriverWait(driver, 15)
search()
jobs = job_card()
scrape_job_details(jobs)
save_jobs(jobs)

