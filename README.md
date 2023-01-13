# สร้าง venv
- python -m venv <foldername>

# เข้าใช้งาน venv
- venv\Scripts\activate

# install flask
- pip install flask

# สร้างตัวเก็บชื่อ library (ถ้าไม่ใส่ > <filename> จะ print ดู lib ที่มีอย่างเดียว) (ไม่ทำก็ได้)
- pip freeze > <filename>.txt

# install ตามไฟล์ .txt (uninstall ก็ได้)
- pip install -r <filename>.txt
