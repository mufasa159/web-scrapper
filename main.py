import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.nytimes.com/section/technology')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='css-1cp3ece')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Author']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='css-1j9dxys e1xfvim30').get_text().replace('\n', '')
        link = post.find('a')['href']
        author = post.find(class_='css-1n7hynb').get_text().replace('\n', '')
        csv_writer.writerow([title, link, author])
