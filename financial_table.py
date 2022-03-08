import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = 'RInger@123',
    database = 'jalshaabh')

cur = cnx.cursor()

#functions
def Display_officerID(officer_id):
    query="SELECT * FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    return result[0]

def Display_grant(officer_id):
    query="SELECT m_given FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "Grant for this area is Rs '{}'".format(result[0])

def Display_salary(officer_id):
    query="SELECT m_salary FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    return "Salary for this area is Rs '{}'".format(result[0])
    
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
