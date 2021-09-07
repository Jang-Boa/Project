from my_app import db
from my_app.scraping.scrap import get_img
from my_app.models.car_model import Car
import pandas as pd
import csv 
import os

# 스크래이핑한 데이터를 csv 파일로 저장
domestics = get_img('N',10) # 국산차 10페이지의 데이터 크롤링
imports = get_img('Y',10) # 수입차 10 페이지의 데이터 크롤링

domestics_table = pd.DataFrame(domestics,columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])
imports_table = pd.DataFrame(imports,columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])

table = pd.concat([domestics_table,imports_table]) # concat two dataframe into one

CSV_FILE_DIR = 'my_app/csv'

# domestics_table.to_csv('{}/table_domestics.csv'.format(CSV_FILE_DIR), encoding='utf-8', mode='w')
# imports_table.to_csv('{}/table_imports.csv'.format(CSV_FILE_DIR), encoding='utf-8', mode='w')
file_name = 'table_car.csv'
table.to_csv('{}/{}'.format(CSV_FILE_DIR,file_name), encoding='utf-8', mode='w')

with open('{}/{}'.format(CSV_FILE_DIR,file_name),encoding='utf-8') as file:
    reader = csv.reader(file,delimiter=',')
    for row in reader: 
        car = Car(id=row[0],name=row[1],company=row[2],importation=row[3],types=row[4],price1=row[5],price2=row[6],fuel_efficiency=row[7],fuel=row[8],image=row[9])
        # attrs = dict(row.items())
        db.session.add(car)
        db.session.commit()
        # db commit이 안됨