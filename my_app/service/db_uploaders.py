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

# def load_csv(db,model,file_name):
def insert_file(model,csv_file_dir, filename):
    with open('{}/{}'.format(csv_file_dir,filename),encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader: 
            query = {}
            for key, value in row.items():
                query[key] = value
            q = model(query)
            # query = model(name=row['names'],
            #             company=row['companies'],
            #             importation=row['car_births'],
            #             types=row['car_types'],
            #             price1=row['car_prices_1'],
            #             price2=row['car_prices_2'],
            #             fuel_efficiency=row['fuel_efficiencies'],
            #             fuel=row['fuels'],
            #             image=row['images'])
            db.session.add(q)
            db.session.commit()
            print('UPLOADED CSV FILE TO DB SUCCESFULLY!')

insert_file(Car,CSV_FILE_DIR,file_name)


"""
sqlalchemy.exc.InterfaceError: (sqlite3.InterfaceError) Error binding parameter 1 - probably unsupported type.
[SQL: INSERT INTO "Car" (name, company, importation, types, price1, price2, fuel_efficiency, fuel, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('2022 캐스퍼', ['companies'], '국산차', '경형', '', '', '정보없음', '가솔린', 'https://imgauto-phinf.pstatic.net/20210901_195/auto_163045763221657AiV_PNG/20210901095324_65Cye5HC.png?type=f160_116')]
(Background on this error at: https://sqlalche.me/e/14/rvf5)
"""