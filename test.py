import glob
import os
from bs4 import BeautifulSoup
import pandas as pd

path = 'D:\\Tests\\scrap_teste\\links'
for filename in glob.glob(os.path.join(path, '*.html')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        html_file = "D:\\Tests\\scrap_teste\\links\\"+filename
        try:
            
            soup = BeautifulSoup(open(html_file), "html.parser")
            right_page = soup.find('table')
            print(right_page.prettify)
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
        
            print(table_data)

        except:
            print("EXCEPTION")
            continue

#create csv
dataframe = pd.DataFrame(data = table_data, columns = table_header)
dataframe.to_csv("test.csv")
