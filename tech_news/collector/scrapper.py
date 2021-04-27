"""LETS GET STARTED"""
import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        res = requests.get(url, timeout=timeout)
        time.sleep(delay)

        if res.status_code != 200:
            return ""

        return res.text

    except requests.Timeout:

        return ""


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
