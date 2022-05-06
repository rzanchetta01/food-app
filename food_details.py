import requests
from bs4 import BeautifulSoup
import pandas as pd

# path to all links of food
# each food will be created a new csv of that data
folder_path = "T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\\links.txt"

table_header = []
table_data = []

# set collumns
table_header.append("Componente")
table_header.append("Unidades")
table_header.append("Valor por 100g")
table_header.append("Colher sopa cheia")
table_header.append("Copo americano duplo(200mL)")
table_header.append("Copo americano pequeno(130mL")
table_header.append("Pedaco Unidade/Fatia (370g)")
table_header.append("Prato fundo (450g)")
table_header.append("Prato raso (350g)")
table_header.append("id")

for line in open(folder_path, 'r').readlines():
        
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

        # get food data
        body = soup.find_all("table")[0].find_all("tr")[1:]

        for element in body:
            sub_data = []
            sub_data.append(food_code)
            # get items of each row
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            
            table_data.append(sub_data)

        


# create csv
dataframe = pd.DataFrame(data = table_data, columns = table_header)
dataframe.to_csv("T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\\foods-details.csv",  sep=";")

