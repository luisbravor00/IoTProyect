import oracledb
import os
from dotenv import load_dotenv
from insert_test import insert_statements

load_dotenv()
dbuser = os.getenv('DATABASE_USER')
dbpswd = os.getenv('DATABASE_PSWD')
dbdir = os.getenv('DIR_LOCATION')
cs = os.getenv('CONN_ST')



print(dbdir)
    
connection = oracledb.connect(config_dir = dbdir,  user= dbuser, 
                              password=dbpswd, dsn=cs, 
                              wallet_location = dbdir, wallet_password=dbpswd)

cursor = connection.cursor()

patients = """CREATE TABLE Patients (
    ID_Patient NUMBER(8) PRIMARY KEY,
    Name VARCHAR2(255) NOT NULL,
    Last_name VARCHAR2(255) NOT NULL,
    Address VARCHAR2(255),
    Age NUMBER(3),
    Phone VARCHAR2(20),
    Email VARCHAR2(255)
)"""

doctors = """CREATE TABLE Doctors (
    ID_Doctor NUMBER(8) PRIMARY KEY,
    Name VARCHAR2(255) NOT NULL,
    Last_name VARCHAR2(255) NOT NULL,
    Phone_num VARCHAR2(20),
    Office_add VARCHAR2(255)
)"""

prescription = """CREATE TABLE Prescription (
    ID_Prescription NUMBER(8) PRIMARY KEY,
    ID_Doctor NUMBER(8) REFERENCES Doctors(ID_Doctor),
    ID_Patient NUMBER(8) REFERENCES Patients(ID_Patient),
    Date_prescribed DATE NOT NULL
)"""

medicine = """CREATE TABLE Medicine (
    ID_Medication NUMBER(8) PRIMARY KEY,
    Name VARCHAR2(255) NOT NULL,
    Active_Ingredient VARCHAR2(255) NOT NULL,
    Dosage_Form NUMBER(1) NOT NULL
)"""

prescription_details = """CREATE TABLE Prescription_Details (
    ID_Detail NUMBER(8) PRIMARY KEY,
    ID_Prescription NUMBER(8) REFERENCES Prescription(ID_Prescription),
    ID_Medication NUMBER(8) REFERENCES Medicine(ID_Medication),
    TIMES_PER_DAY NUMBER(1) NOT NULL,
    DOSE NUMBER(1) NOT NULL
)"""

tables = [patients, doctors, medicine, prescription, prescription_details]
table_names = ['Prescription_Details', 'Medicine', 'Prescription', 'Doctors', 'Patients']
#for table in table_names:
#    print(table)
#    cursor.execute(f'DROP TABLE {table} CASCADE CONSTRAINTS')

for statement in tables:
    cursor.execute(statement)

for i in insert_statements:
     cursor.execute(i)
     connection.commit()

#for i in table_names:
#    print(i)
#    cursor.execute(f'SELECT * FROM {i}')
#    result = cursor.fetchall()
#    for row in result:
#        print(row)
#    print()

# cursor.execute('SELECT table_name FROM user_tables')

# result = cursor.fetchall()
# for row in result:
#     print(row)

cursor.execute(f'SELECT * FROM Prescription_Details')
result = cursor.fetchall()
for row in result:
    print(row)
