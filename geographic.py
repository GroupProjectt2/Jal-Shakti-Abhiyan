import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = 'RInger@123',
    database = 'jalshaabh')
cur = cnx.cursor()

def SearchByPincode(pin):
    querysbp = 'SELECT * FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querysbp)
    datasbp = cur.fetchall()
    return datasbp

def Display_Rainfall():
    querydr = 'SELECT water_rain FROM Geography'
    cur.execute(querydr)
    datadr = cur.fetchall()
    return datadr

def Display_Ground_Water():
    querydgw = 
