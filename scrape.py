import time

import requests
from bs4 import BeautifulSoup


def scrape(until : int):
    for i in range(1, until):
        url = f"https://osu.ppy.sh/teams/{i}"

        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract specific data
            title = soup.select_one("h1").text if soup.select_one("h1") else "No team found"
            titleStrip = title.strip()
            print(f"{i}: {titleStrip}")
            if(titleStrip == "Hibike! Euphonium"):
                print(i)
                break
            
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
        time.sleep(2)

scrape(500)