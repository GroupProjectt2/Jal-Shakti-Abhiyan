import mysql.connector as ms
cny = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345')


cur = cny.cursor()
cur.execute('DROP DATABASE JalShaAbh')
cur.execute('CREATE DATABASE JalShaAbh')
cur.close()

cnx = ms.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'jalshaabh')
cur = cnx.cursor()


def create_tables():
    
    #CREATING TABLES
    
    query_financial = '''CREATE TABLE Financial
    (id_officer varchar(5) PRIMARY KEY,
    name_officer varchar(30) NOT NULL,
    m_given int NOT NULL CHECK (m_given > -1),
    m_salary int,
    m_oper int,
    months int NOT NULL CHECK (months > -1))'''

    cur.execute(query_financial)
    cnx.commit()

    query_geography = '''CREATE TABLE Geography
    (pincode_area int PRIMARY KEY,
    water_rain int NOT NULL CHECK (water_rain > -1),
    water_ground int NOT NULL CHECK (water_ground > 20),
    water_available int NOT NULL,
    water_required int NOT NULL)'''

    cur.execute(query_geography)
    cnx.commit()

    query_officer = '''CREATE TABLE Officer
    (pincode_area int PRIMARY KEY,
    name_area varchar(20) NOT NULL,
    name_officer varchar(20) NOT NULL,
    id_officer varchar(5) REFERENCES Financial(id_officer))
    '''
    cur.execute(query_officer)
    cnx.commit()

    #INSERTING DATA INTO TABLES

    data_financial = '''INSERT INTO Financial VALUES
    ('ID001', 'Mr.Sharma', 500000, 300000, 200000, 6),
    ('ID002', 'Mr.Desai' , 350000, 150000, 200000, 4),
    ('ID003', 'Mr.Arora' , 600000, 400000, 200000, 12),
    ('ID004', 'Mr.Singh' , 750000, 550000, 200000, 18),
    ('ID005', 'Mr.Mehta' , 400000, 200000, 200000, 8)'''

    cur.execute(data_financial)
    cnx.commit()

    data_geography = '''INSERT INTO Geography VALUES
    ('110023', 501.6, 21.11, 750, 1000),
    ('110045', 497.5, 21.56, 700, 750),
    ('110075', 452.4, 24.50, 600, 700),
    ('110085', 478.1, 23.91, 680, 750),
    ('110001', 469.0, 22.34, 650, 700)'''

    cur.execute(data_geography)
    cnx.commit()

    data_officer = '''INSERT INTO Officer VALUES
    ('110023', 'SAROJINI VILLAGE', 'Mr.Sharma', 'ID001'),
    ('110045', 'PALAM VILLAGE'   , 'Mr.Desai' , 'ID002'),
    ('110075', 'DWARKA'          , 'Mr.Arora' , 'ID003'),
    ('110085', 'ROHINI'          , 'Mr.Singh' , 'ID004'),
    ('110001', 'CONNAUGHT PLACE' , 'Mr.Mehta' , 'ID005')'''

    cur.execute(data_officer)
    cnx.commit()

    return
