import requests, lxml
from bs4 import BeautifulSoup

def push_final_sentence():
    return "the quick brown fox jumped over the lazy dog"

def parse_difficulty_for_int(difficulty_tuple):
    return difficulty_tuple[0]

def scrape_site(url="https://randomwordgenerator.com/sentence.php"):
    website = requests.get(url)
    website.raise_for_status() #simple crash check
    soup = BeautifulSoup(website.content, "html.parser")

    sentence = soup.find(id="result")

    final = sentence.find_all("span", class_ = "support-sentence")

    print(final)


scrape_site()

##result > li > div > span