from my_app import db

class User(db.Model): # 데이터 모델을 나타내는 객체 선언
    __tablename__ = 'users' # table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    
    def __repr__(self):
        return f'UserName:{self.username}'

class Login(db.Model): # 데이터 모델을 나타내는 객체 선언
    __tablename__ = 'login' # table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    
    def __repr__(self):
        return f'UserName:{self.username}'