import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://samiachughtai2.blogspot.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='hentry')

for post in posts:
    title = post.find(class_='post-title').get_text().replace('\n', '')
    print(title)