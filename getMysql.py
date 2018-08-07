import pymysql
from job51 import Job

db = pymysql.connect(host='localhost', user='ming', password='ming', port=3306, db='practice')
cursor = db.cursor()
sql = 'SELECT * FROM app_user'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        Job(row).main()
except:
    print('Error')
