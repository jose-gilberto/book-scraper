import schedule
import time

def scraper():
  print('Scrap the books')

def to_database():
  print('Send the data to database')

schedule.every().minute.do(scraper)

while True:
  schedule.run_pending()
  time.sleep(60)