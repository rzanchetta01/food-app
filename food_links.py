import requests
from bs4 import BeautifulSoup
import pandas as pd

#run in every row possible of table, max size = 56
table_data = []
for i in range(1,70):
    
    #create food url
    base_path = "http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina="+str(i)
    path = requests.get(base_path).content

    soup = BeautifulSoup(path, "html.parser")

    body = soup.find_all("table")[0].find_all("a")[1:]

    sub_data = []
    for element in body:
        result = element.get('href')
        result = "http://www.tbca.net.br/base-dados/" + result
        if not sub_data.__contains__(result):
            print(result)
            sub_data.append(result)
    for data in sub_data:
        table_data.append(data)

#create link csv
dataframe = pd.DataFrame(data = table_data)
dataframe.to_csv("T:\\UAM\\DIMAS_MOBILE_APP\\food-app\\links\links.txt")

