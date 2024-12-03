from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time


def find_jobs_emploitunisie():
    # Web scraping of emploitunisie for jobs
    base_url = requests.get("https://www.emploitunisie.com/recherche-jobs-tunisie").text
    soup = BeautifulSoup(base_url, "lxml")
    jobs = soup.find_all("div", class_="card-job-detail")
    # Get the current date in the format dd.mm.yyyy
    now_date = datetime.now().strftime("%d.%m.%Y")

    for index, j in enumerate(jobs):
        # Extract the date from the <time> tag
        job_time_tag = j.find("time")
        if job_time_tag:
            job_date = job_time_tag.text.strip()

            # Compare the extracted date with today's date or any date bel format hetha 'nn.nn.nnnn' but it will not work in older dates bcz of the jobs are not all available in single page , they are paginated
            if job_date == now_date:

                with open(
                    f"extracted_data/job_{index}.txt", "w", encoding="utf-8"
                ) as f:

                    # Job title
                    f.write(f"Job Title: {j.h3.text.strip()}\n")

                    # Company name
                    company_tag = j.find("a", class_="card-job-company company-name")
                    if company_tag:
                        f.write(f"Company Name:, {company_tag.text.strip()}\n")

                    # Job description
                    job_description = j.find("div", class_="card-job-description")
                    if job_description:
                        description_text = job_description.p.text.strip()
                        f.write(f"Job Description: {description_text.strip()}\n")

                    # Skills and other details
                    job_details = j.find("ul")
                    if job_details:
                        f.write(f"Details: {job_details.text.strip()}\n")

                    f.write(f"Post Created At: {job_date}")

                    # f.write("-" * 50)
                print(f"File Saved Successfully ! job_{index}")


# script will be executed every 10 min
if __name__ == "__main__":
    while True:
        find_jobs_emploitunisie()
        time_wait = 10
        print(f" Waiting {time_wait} minutes")
        time.sleep(time_wait * 60)
