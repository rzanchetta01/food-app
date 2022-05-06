import requests
from bs4 import BeautifulSoup
import pandas as pd

# path to all links of food
# each food will be created a new csv of that data
folder_path = "T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\\links.txt"
count = 0
for line in open(folder_path, 'r').readlines():
        
        link = line.split(",")
        print(link[1])
        html_file = requests.get(link[1]).content

        soup = BeautifulSoup(html_file, "html.parser")
        right_page = soup.find('table')

        # get food name/description
        food_title = soup.find('h5', id="overview")
        food_title = food_title.text.strip()
        food_title = food_title.split(": ")

        food_name = food_title[2].split("<<")

        # separete by language
        food_name_pt = food_name[0]
        food_name_en = food_name[1].replace(">", "")


        # get collumns
        table_header = []
        header = soup.find_all("table")[0].find("tr")

        for item in header:
            try:
                table_header.append(item.get_text())
            except:
                continue
        
        table_header.append("nome portugues")
        table_header.append("nome ingles")

        # get items
        table_data = []
        body = soup.find_all("table")[0].find_all("tr")[1:]

        for element in body:
            sub_data = []
            # get items of each row
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            
            sub_data.append(food_name_pt)
            sub_data.append(food_name_en)
            table_data.append(sub_data)

        #create file name
        file_name = folder_path + str(count) + ".csv"

        # create csv
        dataframe = pd.DataFrame(data = table_data, columns = table_header)
        dataframe.to_csv(file_name,  sep=";")
        count = count + 1
