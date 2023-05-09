import requests
import difflib
import time

def get_website_contents(url, headers):
    response = requests.get(url, headers=headers)
    return response.content.decode("utf-8")

def check_for_changes(url, headers, interval):
    old_contents = get_website_contents(url, headers)
    while True:
        time.sleep(interval)
        try:
            new_contents = get_website_contents(url, headers)
        except requests.exceptions.RequestException as e:
            print("Error occurred:", e)
            continue
        similarity = difflib.SequenceMatcher(None, old_contents, new_contents).ratio()
        if similarity < 0.95:
            print("Website has been updated!")
            old_contents = new_contents
        else:
            print("Website has not been updated.")

url = "https://example.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
interval = 60 # seconds
check_for_changes(url, headers, interval)
