import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

# path to all links of food
# each food will be created a new csv of that data
folder_path = "/media/rodrigozanchetta/Trabalhos/UAM/DIMAS_MOBILE_APP/food-app/web scrapper/links/links.txt"

all_collumns = []

# set collumns
for line in open(folder_path, 'r').readlines():

        table_header = []
        table_header.append("codigo")
        table_data = []
        
        #form request url
        link = line.split(",")
        print(link[1])
        html_file = requests.get(link[1]).content

        #get page html
        soup = BeautifulSoup(html_file, "html.parser")

        # get food id
        food_title = soup.find('h5', id="overview")
        food_title = food_title.text.strip()
        food_title = food_title.split(": ")
        food_code = food_title[1]
        food_code = food_code.replace("Descrição", " ")

        header = soup.find_all("table")[0].find("tr")
        for items in header:
            try:
                table_header.append(items.get_text())
                if not all_collumns.__contains__(items.get_text()):
                    all_collumns.append(items.get_text())
            except:
                continue


        # get food data
        body = soup.find_all("table")[0].find_all("tr")[1:]

        for element in body:
            sub_data = []
            sub_data.append(food_code)
            # get items of each row
            count = 1
            for sub_element in element:
                try:
                        sub_data.append(sub_element.get_text())
                except:
                    continue

            else :
                table_data.append(sub_data)

        # create csv
        dataframe = pd.DataFrame(data = table_data, columns = table_header)
        #dataframe.to_csv("/media/rodrigozanchetta/Trabalhos/UAM/DIMAS_MOBILE_APP/food-app/web scrapper/links/foods-details"+food_code+".csv",  sep=";")

columns_df = pd.DataFrame(data=all_collumns)
columns_df.to_json("/media/rodrigozanchetta/Trabalhos/UAM/DIMAS_MOBILE_APP/food-app/web scrapper/links/foods-all-columns.csv")
