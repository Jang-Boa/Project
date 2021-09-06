from flask import Blueprint, render_template, request, redirect
from my_app.models import user_model
from my_app import db
from my_app.models import car_model

bp = Blueprint('main',__name__)

##### HOME PAGE #####
@bp.route('/')
def index():
    """
    Main HomePage
    """
    return render_template('index.html')

##### Register Page #####
@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method =='GET': # GET 방식으로 단순 html 파일을 보여준다. 
        return render_template("register.html")

    else: # POST 
        username = request.form['username']
        password = request.form['password']
        re_password = request.form['re_password']
        
        if not (username and password and re_password):
            return "모두 입력해주세요"
        elif password != re_password:
            return "비밀번호를 확인해주세요"
        elif db.session.query(user_model.User).filter(user_model.User.username == str(username)).first():
            return ("이미 사용중인 아이디 입니다")
        else:
            usertable = user_model.User()
            usertable.username = str(username)
            usertable.password = str(password)
            
            db.session.add(usertable)
            db.session.commit()
            return '회원가입 완료!'
        return redirect('/')

# login 페이지 접속(GET) 처리와, "action=/login" 처리(POST)처리 모두 정의
@bp.route('/login', methods=['GET', 'POST'])	
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
        
		try:
			data = db.session.query(user_model.User).filter_by(user_model.User.username==username, password==password).first()	# ID/PW 조회Query 실행
			if data is not None:	# 쿼리 데이터가 존재하면
				db.session['username'] = username	# userid를 session에 저장한다.
				return redirect('/')
			else:
				return 'Not Registerd'	# 쿼리 데이터가 없으면 출력
		except:
			return "Login Error"	# 예외 상황 발생 시 출력

# logout
@bp.route('/logout', methods=['GET'])
def logout():
	db.session.pop('username', None)
	return redirect('/')

# prefer
@bp.route('/prefer', methods=['GET'])
def prefer():
	return render_template("prefer.html")

# recommend
@bp.route('/prefer/recommend', methods=['GET'])
def recommend():
	return render_template("recommend.html")