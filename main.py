import mariadb
from dotenv import load_dotenv
import os

load_dotenv()

user_name = os.getenv('DB_USER')
password = os.getenv('DB_password')

# 1. Database Connection Parameters
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': user_name,
    'password': password,
    'database': 'sakila'
}
conn =mariadb.connect(**db_config)
cur=conn.cursor()
cur.execute("SELECT*FROM FILM")
res= cur.fetchall()
print(res)
