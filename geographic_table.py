import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = 'RInger@123',
    database = 'jalshaabh')
cur = cnx.cursor()

#module

def SearchByPincode(pin):
    querysbp = 'SELECT * FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querysbp)
    datasbp = cur.fetchall()
    return datasbp

def Display_Rainfall(pin):
    querydr = 'SELECT water_rain FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydr)
    datadr = cur.fetchall()
    return datadr

def Display_Ground_Water(pin):
    querydgw = 'SELECT water_ground FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydgw)
    datadgw = cur.fetchall()
    return datadgw

def Display_Total_Water(pin):
    querydtw = 'SELECT water_available FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydtw)
    datadtw = cur.fetchall()
    return datadtw

def Display_Required_Water(pin):
    querydrw = 'SELECT water_required FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydrw)
    datadrw = cur.fetchall()
    return datadrw
