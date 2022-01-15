import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')

cur = cnx.cursor()

#functions
def Update_pincode(old_pincode,new_pincode):
    query="UPDATE geography, officer SET geography.pincode_area = '{}',officer.pincode_area = '{}' WHERE geography.pincode_area = '{}' AND officer.pincode_area = '{}'".format(new_pincode,new_pincode,old_pincode,old_pincode)
    cur.execute(query)
    cnx.commit()
    print("Successfully updated")
def Display_officer(officer_id):
    query="SELECT * FROM officer WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    print(result)
def Update_officer(officer_id,new_name):
    query="UPDATE officer SET name_officer = '{}' WHERE id_officer = '{}'".format(new_name,officer_id)
    cur.execute(query)
    cnx.commit()
    print("Successfully updated")
def SearchByOfficerID(officer_id):
    query="SELECT name_officer FROM officer WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    print(result)
ans="yes"
while ans=="yes":
    print("Officer Table functions")
    print("1. Update pincode")
    print("2. Fetch details using officer id")
    print("3. Update officer name")
    print("4. Search officer name using officer id")
    choice=int(input("Enter choice:\t"))
    if choice==1:
        old_pincode=input("Enter old pincode:\t")
        new_pincode=input("Enter new pincode:\t")
        Update_pincode(old_pincode,new_pincode)
    elif choice==2:
        o_id=input("Enter officer id:\t")
        Display_officer(o_id)
    elif choice==3:
        o_id=input("Enter officer id:\t")
        new_name=input("Enter new officer name:\t")
        Update_officer(o_id,new_name)
    elif choice==4:
        o_id=input("Enter officer id:\t")
        SearchByOfficerID(o_id)
    ans=input("Enter yes to continue:\t")
