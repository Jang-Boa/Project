import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#                                                     user='etiwesmo', # 사용자 이름
#                                                     pw = 'idzPxGHvVixIhrZ40_Or3GeYPs1MkLPa', # 암호
#                                                     url = 'rosie.db.elephantsql.com', # 데이터베이스 주소
#                                                     db='etiwesmo' # 데이터베이스 이름
#                                                     )

# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://@localhost/test'

SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///{}'.format(os.path.join(BASE_DIR, 'data.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = True