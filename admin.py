import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')

cur = cnx.cursor()

#functions
def Change_officer_name(officer_name,officer_id):
    query="UPDATE financial,officer SET financial.name_officer = '{}', officer.name_officer = '{}' WHERE financial.id_officer = '{}' AND officer.id_officer = '{}'".format(officer_name,officer_name,officer_id,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"

def Update_grant(officer_id,new_grant):
    query="UPDATE financial SET m_given = {} WHERE id_officer = '{}'".format(new_grant,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"
    
def Update_salary(officer_id,new_salary):
    query="UPDATE financial SET m_salary = {} WHERE id_officer = '{}'".format(new_salary,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"

def Update_pincode(old_pincode,new_pincode):
    query="UPDATE geography, officer SET geography.pincode_area = '{}',officer.pincode_area = '{}' WHERE geography.pincode_area = '{}' AND officer.pincode_area = '{}'".format(new_pincode,new_pincode,old_pincode,old_pincode)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"
