from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('books_scraped.csv', 'w')
with csv_file:
    csv_writer = csv.writer(csv_file, delimiter = "|")
    csv_writer.writerow(['bookTitle', 'bookPage', 'bookPrice', 'bookImage'])

    for page in range(1, 51):
        url = 'http://books.toscrape.com/catalogue/page-'+str(page)+'.html'
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        for book in soup.findAll('article', class_='product_pod'):
            bookTitle = book.img['alt']
            bookImage = book.img['src']
            bookPage = 'http://books.toscrape.com/catalogue/'+book.a['href']
            bookPrice = book.find('p', class_='price_color').text
            csv_writer.writerow([bookTitle, bookPage, bookPrice, bookImage])
