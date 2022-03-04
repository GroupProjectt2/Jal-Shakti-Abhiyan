import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')

cur = cnx.cursor()

#functions
def Display_officerID(officer_id):
    query="SELECT * FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    return result

def Display_grant(officer_id):
    query="SELECT m_given FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "Grant for this area is Rs '{}'".format(result[0])
    
def Update_grant(officer_id,new_grant):
    query="UPDATE financial SET m_given = {} WHERE id_officer = '{}'".format(new_grant,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"

def Display_salary(officer_id):
    query="SELECT m_salary FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "Salary for this area is Rs '{}'".format(result[0])

def Update_salary(officer_id,new_salary):
    query="UPDATE financial SET m_salary = {} WHERE id_officer = '{}'".format(new_salary,officer_id)
    cur.execute(query)
    cnx.commit()
    return "Successfully updated"
    
def Display_cost(officer_id):
    query="SELECT m_oper FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "Cost of operations for this area is Rs '{}'".format(result[0])

def Active_months(officer_id):
    query="SELECT months FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "The program has been active for '{}' months".format(result[0])
