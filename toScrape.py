import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'http://books.toscrape.com/'
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract information from the webpage
books = soup.find_all('article', class_='product_pod')

# Print the titles of the books
for book in books:
    title = book.h3.a['title']
    print(title)
