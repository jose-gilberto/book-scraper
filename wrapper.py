from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

urlBase = 'http://books.toscrape.com/catalogue/'
urlCatalogue = 'http://books.toscrape.com/catalogue/page-{}.html'

stars_dict = {
  'One': 1,
  'Two': 2,
  'Three': 3,
  'Four': 4,
  'Five': 5
}

titles = []
prices = []
categories = []
stars = []

for page in range(1, 51, 1):
  print('-' * 10)
  print('Page: {}'.format(page))

  html = urlopen(urlCatalogue.format(page))
  bsObj = BeautifulSoup(html, 'lxml')

  books = bsObj.findAll('article')

  for book in books:
    href = book.find('h3').find('a').get('href')
    book_url = urlBase + href

    print('Book: {}'.format(book_url))

    bsObj2 = BeautifulSoup(urlopen(book_url), 'lxml')
  
    title = bsObj2.find('h1').get_text()
    category = bsObj2.find('ul', class_='breadcrumb').findAll('li')[2].find('a').get_text()
    price = bsObj2.find('p', class_='price_color').get_text().replace('£', '')
    star = stars_dict[bsObj2.find('p', class_='star-rating')['class'][1]]
  
    titles.append(title)
    categories.append(category)
    prices.append(price)
    stars.append(star)

df = pd.DataFrame({
  'title': titles,
  'category': categories,
  'price': prices,
  'stars': stars
})

df.to_csv('./books.csv')



  
