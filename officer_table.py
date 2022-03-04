import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')

cur = cnx.cursor()

def Update_pincode(old_pincode,new_pincode):
    query="UPDATE geography, officer SET geography.pincode_area = '{}',officer.pincode_area = '{}' WHERE geography.pincode_area = '{}' AND officer.pincode_area = '{}'".format(new_pincode,new_pincode,old_pincode,old_pincode)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"

def Display_officer(officer_id):
    query="SELECT * FROM officer WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    return result
def Update_officer(officer_id,new_name):
    query="UPDATE officer SET name_officer = '{}' WHERE id_officer = '{}'".format(new_name,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"
def SearchByOfficerID(officer_id):
    query="SELECT name_officer FROM officer WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    return result
