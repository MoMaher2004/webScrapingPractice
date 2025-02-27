'''
this code will search for today's matches on yallakora.com and print it
it is a very basic web scraping project
'''

import requests
from bs4 import BeautifulSoup
import csv

url = f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA'
page = requests.get(url)
pageContent = BeautifulSoup(page.content, 'lxml')

matchCards = pageContent.find_all('div', {'class': 'matchCard'})

matches = []
'''
{
tourner
team-a
team-b
time
}
'''

for card in matchCards:
    tourner = card.find('div', {'class': 'title'}).find('h2').getText()
    tournerList = card.find('div', {'class': 'ul'}).find_all('div', {'class': 'liItem'})
    for item in tournerList:
        match = {
            'tourner': tourner,
            'teamA': item.find('div', {'class': 'teamsData'}).find('div', {'class': 'teamA'}).find('p').getText(),
            'teamB': item.find('div', {'class': 'teamsData'}).find('div', {'class': 'teamB'}).find('p').getText(),
            'time': item.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).getText(),
        }
        matches.append(match)

print(matches)
