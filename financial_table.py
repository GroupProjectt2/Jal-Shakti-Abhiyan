import mysql.connector as ms
cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')
if cnx.is_connected():
    print("Successfully connected!")

cur = cnx.cursor()

#functions
def Display_officerID(officer_id):
    query="SELECT * FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchall()
    print(result)

def Display_grant(officer_id):
    query="SELECT m_given FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    print("Grant for this area is Rs",result[0])
    
def Update_grant(officer_id,new_grant):
    query="UPDATE financial SET m_given = {} WHERE id_officer = '{}'".format(new_grant,officer_id)
    cur.execute(query)
    cnx.commit()
    print("Successfully updated")

def Display_salary(officer_id):
    query="SELECT m_salary FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    print("Salary for this area is Rs",result[0])

def Update_salary(officer_id,new_salary):
    query="UPDATE financial SET m_salary = {} WHERE id_officer = '{}'".format(new_salary,officer_id)
    cur.execute(query)
    cnx.commit()
    print("Successfully updated")
    
def Display_cost(officer_id):
    query="SELECT m_oper FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    print("Cost of operations for this area is Rs",result[0])

def Active_months(officer_id):
    query="SELECT months FROM financial WHERE id_officer = '{}'".format(officer_id)
    cur.execute(query)
    result=cur.fetchone()
    print("The program has been active for",result[0],"months")

#Menu
ans="yes"
while ans=="yes":
    print("Financial Table functions")
    print("1. Fetch details using officer id")
    print("2. Fetch money granted")
    print("3. Update money granted")
    print("4. Display salary of workers")
    print("5. Update salary of workers")
    print("6. Display cost of operations")
    print("7. Display active months")
    choice=int(input("Input choice:\t"))
    if choice==1:
        o_id=input("Enter officer id:\t")
        Display_officerID(o_id)
    elif choice==2:
        o_id=input("Enter officer id:\t")
        Display_grant(o_id)
    elif choice==3:
        o_id=input("Enter officer id:\t")
        new_grant=input("Enter new grant:\t")
        Update_grant(o_id,new_grant)
    elif choice==4:
        o_id=input("Enter officer id:\t")
        Display_salary(o_id)
    elif choice==5:
        o_id=input("Enter officer id:\t")
        new_salary=input("Enter new salary:\t")
        Update_salary(o_id,new_salary)
    elif choice==6:
        o_id=input("Enter officer id:\t")
        Display_cost(o_id)
    elif choice==7:
        o_id=input("Enter officer id:\t")
        Active_months(o_id)
    ans=input("Press yes to continue:\t")
