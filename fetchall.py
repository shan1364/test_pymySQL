import pymysql
import sys
import traceback
 
# 連接 db
db = pymysql.connect(
    host="localhost",
    user="user",
    passwd="pws",
    db="TESTDB",
    cursorclass=pymysql.cursors.DictCursor)
 
# 使用 cursor() 方法創建一個游標對象 cursor
cursor = db.cursor()

# SQL 查詢語句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
try:
    cursor.execute(sql)
    # 取得所有資料
    results = cursor.fetchall()    
    
    for row in results:
        fname = row['FIRST_NAME']
        lname = row['LAST_NAME']
        age = row['AGE']
        sex = row['SEX']
        income = row['INCOME']
        print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income ))

except Exception as e:
    db.rollback()
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)

finally:
    # 關閉 db連接
    db.close()