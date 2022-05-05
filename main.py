import requests
from bs4 import BeautifulSoup
import pandas as pd


folder_path = "D:\Tests\scrap_teste\links\links.txt"
count = 0
for link in open(folder_path, 'r').readlines():

    html_file = requests.get(link).content

    soup = BeautifulSoup(html_file, "html.parser")
    right_page = soup.find('table')

    #get food name/description
    food_title = soup.find('h5', id="overview")
    food_title = food_title.text.strip()
    food_title = food_title.split(": ")

    food_name = food_title[2].split("<<")

    #separete by language
    food_name_pt = food_name[0]
    food_name_en = food_name[1].replace(">", "")


    #get collumns
    table_header = []
    header = soup.find_all("table")[0].find("tr")

    for item in header:
        try:
            table_header.append(item.get_text())
        except:
            continue


    #get items
    table_data = []
    body = soup.find_all("table")[0].find_all("tr")[1:]

    for element in body:
        sub_data = []
        #get items of each row
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        table_data.append(sub_data)


    file_name = folder_path + str(count) + ".csv"

    #create csv
    dataframe = pd.DataFrame(data = table_data, columns = table_header)
    dataframe.to_csv(file_name)
    count = count + 1