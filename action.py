import mysql.connector as ms
import random

cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')
cur = cnx.cursor()

def action_advice(inp):
    
    action_select = '''SELECT pincode_area, water_available, water_required FROM Geography'''

    cur.execute(action_select)

    data = cur.fetchall()

    found = False
    for row in data:
        if int(row[0]) == inp:
            found = True
            diff = int(row[2])-int(row[1])
    if found == False:
        return 'That is an invalid pincode!'
        
    advice = ['Spread awareness among the resident population about water conservation',
              'Develop watersheds',
              'Set up more rainwater harvesting locations',
              'Plant trees around the area',
              'Renovate existing water bodies/tanks',]
    if diff > 0:
        adv = advice[random.randrange(0,len(advice))]
        return adv
    else:
        return '\nAdequate water is available in the region.\nGreat work!'
