from bs4 import BeautifulSoup
import cloudscraper
import sys

sys.stdout=open("list.txt","w", encoding="utf-8")

scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
url = 'https://www.your.url/index.php'
req = scraper.get(url)
soup = BeautifulSoup(req.content,'lxml')
ürünler = soup.find_all("div", {"class": "row row-cols-2 row-cols-lg-6 row-cols-md-4 row-cols-sm-2 m-0 p-0 performer-list"})

for ürün in ürünler:
    ürün_linkleri = ürün.find_all("div",attrs={"class":"d-flex h-100 w-100 start-0 bottom-0 z-index-1 grad-bg align-items-end"})
    for i in ürün_linkleri:
        link = i.find("span",attrs={"class":"online-member-title"})
        
    for a in ürün_linkleri:
        link = a.find("strong")
        print(link)
sys.stdout.close()
