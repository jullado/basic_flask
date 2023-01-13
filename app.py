from flask import Flask , request, Blueprint, jsonify
import os
from dotenv import load_dotenv
import requests, json

load_dotenv()   # ทำให้ใช้ค่า env จากไฟล์ .env ได้ด้วย os.getenv

PORT = os.getenv("PORT" , default="3000") # default จะใช้ตอนรัน local ถ้า prod จะเรียก env


# เรียกใช้ flask **************************************************
app = Flask(__name__)


# ส่วนที่ทำงานก่อนส่ง response กลับไป  (ส่วนใหญ่ใช้จัดการ core origin, credential) **************************************************
@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin',
        '*'
        # 'http://localhost:4200',

    )
    response.headers.add(
        'Access-Control-Allow-Credentials',
        'true'
    )
    return response


# กำหนด route path เปล่า (ไม่มีก็ได้)**************************************************
@app.route('/')
def home(): # func ที่ทำงานใน path เปล่า
    return "Hello My First Page"


# ฟังก์ชันสำหรับใช้ใน path ลูก **************************************************
def test_path1():
    params = request.args # get all params ถ้าต้องการ key เดียว ใส่ .get("key")
    return jsonify({"status":"success","message": "Test Path 1", "data" : params})

def test_path2():
    body = request.json # รับค่า body ทั้งหมด
    return jsonify({"status":"success","message": "Test Path 2", "data" : body})

def test_request():
    payload = { "username" : "julladith"}

    url = "http://127.0.0.1:8080/request/get"
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.request("GET", url, headers=headers, data=json.dumps(payload))   # แปลงจาก dict เป็น json เพื่อส่ง
    print(res.text)

    return jsonify({"status":"success","message": "Test send request"})

routes = Blueprint('test',__name__) # สร้าง blueprint สำหรับเพิ่ม path ลูก

routes.add_url_rule('/test1','test1', test_path1, methods = ['GET']) # เพิ่ม path ลูก ให้ blueprint
routes.add_url_rule('/test2','test2', test_path2, methods = ['POST']) # เพิ่ม path ลูก ให้ blueprint
routes.add_url_rule('/test_request','test_request', test_request, methods = ['POST'])
            
app.register_blueprint(routes, url_prefix="/api/v1") # group path


# ถ้าไฟล์นี้ถูกสั่งรัน __name__ จะเท่ากับ __main__ **************************************************
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=PORT,debug=True) # สร้าง flask connection
    
    # default => host=ipv4, port=5000, debug=false
    # ถ้า debug=True จะสามารถทำ hot reload ได้