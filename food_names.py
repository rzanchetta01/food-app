import requests
from bs4 import BeautifulSoup
import pandas as pd

folder_path = "T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\\links.txt"

table_header = ["id", "nome_pt-br", "name_en-us"]
table_data = []

for line in open(folder_path, 'r').readlines():
    
    #form request url
    link = line.split(",")
    print(link[1])
    html_file = requests.get(link[1]).content

    #get page html
    soup = BeautifulSoup(html_file, "html.parser")
    
    # get food name/descriptio and id
    food_title = soup.find('h5', id="overview")
    food_title = food_title.text.strip()
    food_title = food_title.split(": ")
    
    food_name = food_title[2].split("<<")
    food_code = food_title[1]
    food_code = food_code.replace("Descrição", " ")


    # separete by language
    food_name_pt = food_name[0]
    food_name_en = food_name[1].replace(">", "")

    sub_data = []
    sub_data.append(food_code)
    sub_data.append(food_name_pt)
    sub_data.append(food_name_en)
    table_data.append(sub_data)


# create csv
dataframe = pd.DataFrame(data = table_data, columns = table_header)
dataframe.to_csv("T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\\foods-name.csv",  sep=";")