from my_app import db

class Car(db.Model): # 데이터 모델을 나타내는 객체 선언
    __tablename__ = 'Car' # table name

    id = db.Column(db.Integer, primary_key=True)
    carname = db.Column(db.String(32), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    people = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(32), nullable=False)
    fule = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(32), nullable=False)
    