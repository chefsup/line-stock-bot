import requests
from bs4 import BeautifulSoup

def get_news_summary():
    urls = [
        "https://www.investing.com/",
        "https://finance.yahoo.com/",
        "https://www.tradingview.com/"
    ]

    headlines = []
    for url in urls:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            text = tag.get_text().strip()
            if len(text) > 40:
                headlines.append(text)
            if len(headlines) >= 3:
                break

    summary = "\n- " + "\n- ".join(headlines[:3])
    return summary