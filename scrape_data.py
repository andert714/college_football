from pandas import DataFrame
from requests import get
from bs4 import BeautifulSoup

url = 'https://www.sports-reference.com/cfb/years/2020-schedule.html'
html = get(url).content
soup = BeautifulSoup(html, 'html.parser')
table = soup('table', {'id': 'schedule'})[0]

headers = ['week', 'date', 'time', 'day', 'winner', 'winner_pts', 'home', 'loser', 'loser_pts', 'notes']
body = [[i.text for i in row('td')] for row in table('tr', class_= lambda x: x != 'thead')][1:]

df = DataFrame(data = body, columns=headers)
df.to_csv('data/2020.csv', index=False)
