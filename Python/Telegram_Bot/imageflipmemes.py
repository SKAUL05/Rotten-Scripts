import random
from bs4 import BeautifulSoup
import requests

#The imageflip website is used to scrape the urls of memes.
#A random url is returned

def memes():
    tenpages = []
    for page_no, _ in enumerate(range(10), start=1):
        url = f"https://imgflip.com/tag/memes?page={str(page_no)}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        for d in (soup.find('div', attrs={"id":"page" , "class":"base clearfix"}).find('div', attrs={"id":"base-left"}).find_all("div" , attrs={"class":"base-unit clearfix"})):
            p = (d.find("div" , attrs = {"class":"base-img-wrap-wrap"}).find('img'))
            try:
                tenpages.append("https:" + str(p['src']))
            except:
                pass
    return(random.choice(tenpages))

if __name__ == "__main__":
    print(memes())
