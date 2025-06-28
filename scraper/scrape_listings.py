import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_remoteok():
    url = "https://remoteok.com/api"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()[1:]  # Skip metadata
        jobs = []

        for job in data:
            jobs.append({
                "title": job.get("position"),
                "company": job.get("company"),
                "location": job.get("location"),
                "url": job.get("url")
            })

        df = pd.DataFrame(jobs)
        df.to_csv("data/listings.csv", index=False)
        print("✅ Data saved to listings.csv")
    else:
        print(f"❌ Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    scrape_remoteok()
