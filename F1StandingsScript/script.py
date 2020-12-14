import requests
from bs4 import BeautifulSoup
from texttable import *

goodYear = False
year = 2020
while not goodYear:
    goodYear = True
    yearString = input('Please input a year( between 1950 and 2020): ')
    try:
        year = int(yearString)
    except ValueError:
        print('Wrong year! Try again!')
        goodYear = False
    if year < 1950 or year > 2020:
        goodYear = False

URL = 'https://www.formula1.com/en/results.html/' + str(year) + '/drivers.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

standings_table = soup.find(class_='resultsarchive-table')

standings_row = standings_table.find_all('tr')

drivers = []
for index in range(1, len(standings_row)):
    row = standings_row[index]
    driver_first_name = row.find('span', class_='hide-for-tablet').text.strip()
    driver_second_name = row.find('span', class_='hide-for-mobile').text.strip()
    points = row.find('td', class_='dark bold').text.strip()
    position = row.find('td', class_='dark').text.strip()
    team = row.find('a', class_='grey semi-bold uppercase ArchiveLink').text.strip()
    drivers.append([position, driver_first_name, driver_second_name, team, points])

print(f'                     {year} DRIVER STANDINGS')
table = Texttable()
table.header(["Position", "First name", "Second name", "Car", "Points"])
table.set_cols_align(['l', 'c', 'c', 'c', 'c'])
for driver in drivers:
    table.add_row(driver)
table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.HLINES)
print(table.draw())
