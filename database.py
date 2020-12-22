import mysql.connector

db=mysql.connector.connect(host="localhost",user="agraroller",passwd="root12345678",database="agraroller_database")

cursor=db.cursor()

y=cursor.execute("SELECT * FROM allot")
print(y)

def create_tables():
    cursor.execute("DROP TABLE IF EXISTS LOGIN_INFO")
    cursor.execute("DROP TABLE IF EXISTS LOCATION_DATA")
    cursor.execute("DROP TABLE IF EXISTS ALLOT")
    db.commit()
    cursor.execute("CREATE TABLE ALLOT(SNO INTEGER,EMPLOPYEE_NAME TEXT,IMEI TEXT)")
    cursor.execute("CREATE TABLE LOGIN_INFO(PROTOCOL_NUMBER TEXT,TERMINAL_ID TEXT,INFORMATION_SERIAL_NUMBER TEXT)")
    cursor.execute("CREATE TABLE LOCATION_DATA(TERMINAL_ID TEXT, DATE_TIME TEXT,LATITUDE INTEGER,LONGITUDE INTEGER,SPEED TEXT,COURSE_STATUS TEXT,MCC TEXT,MNC TEXT,LAC TEXT,CELL_ID TEXT,SERIAL_NUMBER TEXT)")
    return

def login_insert(protocal_number,terminal_id,serial_number):
    cursor.execute("INSERT INTO LOGIN_INFO(PROTOCOL_NUMBER,TERMINAL_ID,INFORMATION_SERIAL_NUMBER)VALUES(%s,%s,%s)",(protocal_number,terminal_id,serial_number))
    db.commit()
    return

def update(employee_name,imei):
    cursor.execute("UPDATE ALLOT SET IMEI = %s WHERE EMPLOPYEE_NAME = %s",(imei,employee_name))
    db.commit()
    return

    

#cursor.execute("INSERT INTO ALLOT(SNO,EMPLOPYEE_NAME,IMEI)VALUES(1,'Kushagra','123456789012345')")
#db.commit()

#create_tables()

