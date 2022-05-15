import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# path to all links of food
# each food will be created a new csv of that data
folder_path = "/home/rodrigozanchetta/PROJECTS/DIMAS_MOBILE_APP/food-app/web scrapper/links/links.txt"



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

       # get food name/descriptio and id
        food_title = soup.find('h5', id="overview")
        food_title = food_title.text.strip()
        food_title = food_title.split(": ")
        
        food_name = food_title[2].split("<<")
        food_code = food_title[1]
        food_code = food_code.replace("Descrição", " ")


        # separete by language
        food_name_pt = food_name[0]
        food_name_en = ""
        if len(food_name) > 1:
            food_name_en = food_name[1].replace(">", "")



        #t head
        header = soup.find_all("table")[0].find("tr")
        for items in header:

            if table_header.__contains__(items.get_text()):
                aux_items = items.get_text() + "_2"
                table_header.append(aux_items)

            else:
                table_header.append(items.get_text())



        #t body
        body = soup.find_all("table")[0].find_all("tr")[1:]

        for element in body:
            sub_data = []
            sub_data.append(food_code)
            # get items of each row
            for sub_element in element:

                sub_data.append(sub_element.get_text())
            
            table_data.append(sub_data)

        
        # export data
        dataframe = pd.DataFrame(data = table_data, columns = table_header)

        info_data = [{"name-ptbr": food_name_pt},{"name-eng": food_name_en},{"codigo": food_code}]
     
        json_path= "/home/rodrigozanchetta/PROJECTS/DIMAS_MOBILE_APP/food-app/web scrapper/links/foods/food_"+food_code+".json"
        dataframe.to_json(json_path)


        with open(json_path, "r") as file:
            data = json.load(file)
       
        data["Info_Data"] = info_data
        
        with open(json_path, "w") as file:
            json.dump(data, file)
