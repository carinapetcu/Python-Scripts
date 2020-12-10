import requests
from bs4 import BeautifulSoup
from texttable import *

URL = 'https://www.formula1.com/en/results.html/2020/drivers.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

standings_table = soup.find(class_='resultsarchive-table')

standings_row = standings_table.find_all('tr')

drivers = []
for index in range(1, len(standings_row)):
    row = standings_row[index]
    driver_first_name = row.find('span', class_='hide-for-tablet').text.strip()
    driver_second_name = row.find('span', class_='hide-for-mobile').text.strip()
    driver_initials = row.find('span', class_='uppercase hide-for-desktop').text.strip()
    position = row.find('td', class_='dark').text.strip()
    team = row.find('a', class_='grey semi-bold uppercase ArchiveLink').text.strip()
    drivers.append([position, driver_first_name, driver_second_name, driver_initials, team])

table = Texttable()
table.header(["Position", "First name", "Second name", "Initials", "Car"])
table.set_cols_align(['l', 'c', 'c', 'c', 'c'])
for driver in drivers:
    table.add_row(driver)
table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.HLINES)
print(table.draw())
