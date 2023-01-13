## สร้าง venv
python -m venv \<folder_name\>

## เข้าใช้งาน venv
\<folder_name\>\Scripts\activate

## install ตามไฟล์ .txt (uninstall ก็ได้)
pip install -r requirements.txt

## สร้างตัวเก็บชื่อ library (ถ้าไม่ใส่ > <filename> จะ print ดู lib ที่มีอย่างเดียว) (ไม่ทำก็ได้)
pip freeze > requirements.txt

## Run app
python app.py
