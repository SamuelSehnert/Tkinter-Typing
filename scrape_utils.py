import requests, lxml
from bs4 import BeautifulSoup

    
def scrape_site(url="https://www.randomwordgenerator.org/random-sentence-generator"):
    website = requests.get(url)
    website.raise_for_status() #simple crash check
    soup = BeautifulSoup(website.text, "lxml")

    final = soup.select("body > div.container.container-1.index > div > div.row.no-margin.for-up > div.col-md-6.col-sm-6.col-xs-12.show-content > ul > li > p.result > b")
    final = str(final[0])
    final = final[3:len(final) - 4]

    return final

def scrape_sentences(level):
    sentences = []
    while len(sentences) < level + 1:
        sentence = scrape_site()
        if len(sentence) < 40:
            sentences.append(sentence)

    return " ".join(sentences)



