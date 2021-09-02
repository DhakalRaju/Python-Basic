# send request and get the response (string format)
# convert the string format response into HTML format (parse)
# request the required information

import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.ycombinator.com/')

# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())
# print(soup.title.text)
# print(soup.find('a'))
# print(len(soup.find_all('a')))
# print(soup.find_all('a')[200])
# print(soup.find_all('a')[0].get('href'))

# all_a = soup.find_all('a')
# print(all_a[0].text)
# print(all_a[0].get('href'))
# print(all_a)

# all_a = soup.select('.storylink')
news_list = all_a = soup.select('.storylink')
# news_list = all_a = soup.find_all('a', _class = 'storylink')
# print(all_a)

with open('news.txt', 'w') as f:
    for news in news_list:
        # print(news.text)
        f.write(news.text)
        f.write('  ')
        f.write(news.get('href'))
        f.write('\n')
        f.write('*' * 15)
        f.write('\n')

        # print(news.get('href'))
        # print('*' * 20)




# for item in all_a:
    # print(item)