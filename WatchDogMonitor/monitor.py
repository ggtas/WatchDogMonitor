import time
import requests

URLS = [
    "https://example.com",
]

CHECK_INTERVAL = 10

def check_urls():
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            print(f"[OK] {url} -> {response.status_code}")
        except Exception as e:
            print(f"[FAIL] {url} -> {e}")

if __name__ == "__main__":
    while True:
        check_urls()
        time.sleep(CHECK_INTERVAL)
