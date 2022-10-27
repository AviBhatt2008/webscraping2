from re import T
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
soup = BeautifulSoup(page.content, "html.parser")

headers = ["name", "radius", "mass", "distance"]


for index, table in enumerate(soup.find_all("table")):
    if index == 7:
        data_table = table

star_name = []
star_distance = []
star_mass = []
star_radius = []

star_data_unfiltered = []

table_rows = data_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    star_data_unfiltered.append(row)

for i in range(1, len(star_data_unfiltered)):
    star_name.append(star_data_unfiltered[i][0])
    star_distance.append(star_data_unfiltered[i][5])
    star_mass.append(star_data_unfiltered[i][7])
    star_radius.append(star_data_unfiltered[i][8])

final_data = []

for i in range(len(star_name)):
    planet_data = []

    planet_data.append(star_name[i])
    planet_data.append(star_distance[i])
    planet_data.append(star_mass[i])
    planet_data.append(star_radius[i])

    final_data.append(planet_data)

df = pd.DataFrame(data = final_data, columns = headers)
df.to_csv("main.csv")