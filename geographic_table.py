import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
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

#def Display_Ground_Water():
    #querydgw = 

ans="yes"
while ans=="yes":
    print("Geography table functions")
    print("1. Fetch details using pincode")
    print("2. Display annual rainfall")
    print("3. Display ground water")
    print("4. Display total available water")
    print("5. Display water required")
    choice=int(input("Enter choice:\t"))
    if choice==1:
        pin=input("Enter pincode:\t")
        print(SearchByPincode(pin))
    '''elif choice==2:
    elif choice==3:
    elif choice==4:
    elif choice==5:
    '''
    ans=input("Press yes to continue:\t")
