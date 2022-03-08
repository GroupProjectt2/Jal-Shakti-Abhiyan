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
    return datasbp[0]

def Display_Rainfall(pin):
    querydr = 'SELECT water_rain FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydr)
    datadr = cur.fetchone()
    return "Annual Rainfall in this area is '{}' mm".format(datadr[0])

def Display_Ground_Water(pin):
    querydgw = 'SELECT water_ground FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydgw)
    datadgw = cur.fetchone()
    return "Ground water level in this area is '{}' m/bgl".format(datadgw[0])

def Display_Total_Water(pin):
    querydtw = 'SELECT water_available FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydtw)
    datadtw = cur.fetchone()
    return "Total useable water in this area is '{}' KL".format(datadtw[0])

def Display_Required_Water(pin):
    querydrw = 'SELECT water_required FROM Geography WHERE pincode_area = "{}"'.format(pin)
    cur.execute(querydrw)
    datadrw = cur.fetchone()
    return "Total useable water required in this is '{}' KL".format(datadrw[0])
