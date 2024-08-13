import os
import pyupbit
import pymysql
import dotenv


dotenv.load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')


db = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
cursor = db.cursor()


