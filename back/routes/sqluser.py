from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# กำหนด URL ของฐานข้อมูล SQLite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///back/users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Y3T1\Pratical\practical_project\back\users.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# สร้างอ็อบเจ็กต์ของ SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # กำหนดชื่อตารางเป็น 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

# Route สำหรับการลงทะเบียนผู้ใช้
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    
    db.session.add(new_user)  # เพิ่มข้อมูลใหม่ลงในฐานข้อมูล
    db.session.commit()       # บันทึกการเปลี่ยนแปลง
    return jsonify({"message": "User registered successfully"})

if __name__ == '__main__':
    # ใช้ application context เพื่อสร้างตาราง
    with app.app_context():
        db.create_all()  # สร้างตารางในฐานข้อมูล
        print("Database tables created successfully.")  # เพิ่มข้อความนี้
    app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS  # นำเข้า CORS
# from werkzeug.security import generate_password_hash, check_password_hash

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS  # นำเข้า CORS

# app = Flask(__name__)
# # CORS(app)  # เปิดใช้งาน CORS ให้กับแอปพลิเคชันทั้งหมด
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# # ตั้งค่าฐานข้อมูลตามที่คุณต้องการ
# app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Y3T1\Pratical\practical_project\back\users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # กำหนด model User ตามที่เคยกำหนดไว้
# class User(db.Model):
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)

#     def __init__(self, username, email, password_hash):
#         self.username = username
#         self.email = email
#         self.password_hash = password_hash

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     # hashed_password = generate_password_hash(data['password'], method='sha512')

#     new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User registered successfully"})

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         print("Database tables created successfully.")
#     app.run(debug=True)
