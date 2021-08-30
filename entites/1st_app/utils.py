import validators
from bs4 import BeautifulSoup
import requests


def extract_tags_text(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    title = soup.title.text
    desc = soup.find("meta", attrs={"name": "description"})
    desc = desc.get("content", "")
    return title + " " + desc

def is_url(text):
    if validators.url(text.strip()):
        return True
    else:
        return False