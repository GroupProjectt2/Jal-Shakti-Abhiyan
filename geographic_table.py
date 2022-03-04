import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')
cur = cnx.cursor()

#module

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
    querydgw = 'SELECT water_ground FROM Geography'
    cur.execute(querydgw)
    datadgw = cur.fetchall()
    return datadgw

def Display_Total_Water():
    querydtw = 'SELECT water_available FROM Geography'
    cur.execute(querydtw)
    datadtw = cur.fetchall()
    return datadtw

def Display_Required_Water():
    querydrw = 'SELECT water_required FROM Geography'
    cur.execute(querydrw)
    datadrw = cur.fetchall()
    return datadrw
