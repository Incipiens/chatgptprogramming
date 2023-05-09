from bs4 import BeautifulSoup
import requests
import time

def get_website_contents(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract the text content of the website
    return soup.get_text()

def check_for_changes(url, headers, interval):
    old_contents = get_website_contents(url, headers)
    while True:
        time.sleep(interval)
        try:
            new_contents = get_website_contents(url, headers)
        except requests.exceptions.RequestException as e:
            print("Error occurred:", e)
            continue
        if old_contents != new_contents:
            print("Website has been updated!")
            old_contents = new_contents
        else:
            print("Website has not been updated.")

url = "https://www.daft.ie/property-for-sale/south-co-dublin-dublin?sort=publishDateDesc"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
interval = 5 # seconds
check_for_changes(url, headers, interval)
