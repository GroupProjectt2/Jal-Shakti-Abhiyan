import mysql.connector as ms
import random

def action_advice(diff):
    advice = ['Spread awareness among the resident population about water conservation',
              'Develop watersheds',
              'Set up more rainwater harvesting locations',
              'Plant trees around the area',
              'Renovate existing water bodies/tanks',]
    if diff > 0:
        print('\nNot enough water is available in the region.\nConsider taking the following actions:\n')
        print(advice[random.randrange(0,len(advice))])
        return
    else:
        print('\nAdequate water is available in the region.\nGreat work!')
        return

cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = 'RInger@123',
    database = 'jalshaabh')
cur = cnx.cursor()

action_select = '''
SELECT pincode_area,
       water_available, 
       water_required 
       FROM Geography'''

cur.execute(action_select)

data = cur.fetchall()

cont = True
while cont == True:
    inp = int(input('\nPlease enter the pincode of an area:\t'))
    found = False
    for row in data:
        if int(row[0]) == inp:
            found = True
            water_diff = int(row[2])-int(row[1])
            action_advice(water_diff)
    if found == False:
        print('\nThat is an invalid pincode!')
    cont = str(input('\nDo you want to continue? (y/n) :\t'))
    if cont.lower() == 'n':
        cont = False
    else:
        cont = True
