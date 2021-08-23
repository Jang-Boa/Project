## 이 프로젝트는 2021.08.22 자동차 추천 시스템을 만들기 위해 시작하였습니다. ##
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy() # 전역 변수로 db 객체 생성
migrate = Migrate() # 전역 변수로 migrate 객체 생성

def create_app():
    app = Flask(__name__)

    app.secret_key = 'random_string'
    # app.config['SECRET_KEY'] = '...'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite://...db' # sqlite
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object(config) # config.py 파일에 작성한 항목을 환경변수로 부르기

    # ORM
    with app.app_context(): # db 와 migrate 객체 초기화 
        db.init_app(app)
        migrate.init_app(app,db)
    from . import models # 생성한 모델을 플라스크의 migrate 기능이 인식할 수 있도록 모델 가져오기


    # blueprint -> route
    from my_app.routes import main_route
    app.register_blueprint(main_route.bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
