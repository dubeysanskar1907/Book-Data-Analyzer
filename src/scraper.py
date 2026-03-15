import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

books_data = []

for page in range(1,6):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    books = soup.find_all("article",class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p",class_="price_color").text

        rating = book.p["class"][1]

        availability = book.find("p",class_="instock availability").text.strip()

        books_data.append([title,price,rating,availability])

df = pd.DataFrame(books_data,columns=["Title","Price","Rating","Availability"])

df.to_csv("data/books.csv",index=False)

print("scrapping completed")