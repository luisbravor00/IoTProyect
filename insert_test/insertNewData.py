from insert_test import generate_random_number
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

patients_ids = [generate_random_number() for _ in range(5)]
doctors_ids = [generate_random_number() for _ in range(5)]
medicines_ids = [generate_random_number() for _ in range(5)]
prescriptions_ids = [generate_random_number() for _ in range(5)]
prescriptionDetail_ids = [generate_random_number() for _ in range(5)]


patients = [
    ('Michael', 'Johnson', '567 Cedar Ln', 28, '345-678-9012', 'michael.johnson@outlook.com'),
    ('Sarah', 'Garcia', '890 Walnut St', 35, '456-789-0123', 'sarah.garcia@gmail.com'),
    ('Daniel', 'Martinez', '234 Birch St', 45, '567-890-1234', 'daniel.martinez@outlook.com'),
    ('Amanda', 'Lee', '678 Pine St', 31, '678-901-2345', 'amanda.lee@icloud.com'),
    ('Christopher', 'Lopez', '901 Elm St', 27, '789-012-3456', 'christopher.lopez@gmail.com')
]

doctors = [
    ('Olivia', 'Anderson', '345-678-9012', '987 Hilltop Ave'),
    ('James', 'Taylor', '456-789-0123', '654 Sunset Blvd'),
    ('Emma', 'Moore', '567-890-1234', '321 Ocean Dr'),
    ('William', 'Jackson', '678-901-2345', '876 Park Ln'),
    ('Sophia', 'Thomas', '789-012-3456', '543 River Rd')
]

medicines = [
    ('Advil', 'Ibuprofen', 1),
    ('Allegra', 'Fexofenadine', 2),
    ('Benadryl', 'Diphenhydramine', 1),
    ('Claritin', 'Loratadine', 2),
    ('Tylenol', 'Acetaminophen', 1)
]

prescriptionDetails = [
    (3, 2),
    (2, 3),
    (1, 2),
    (2, 1)
]

patient_insert = "INSERT INTO Patients (ID_Patient, Name, Last_Name, Address, Age, Phone, Email) VALUES ({}, '{}', '{}', '{}', {}, '{}', '{}')"
doctor_insert = "INSERT INTO Doctors (ID_Doctor, Name, Last_name, Phone_num, Office_add) VALUES ({}, '{}', '{}', '{}', '{}')"
medicine_insert = "INSERT INTO Medicine (ID_Medication, Name, Active_Ingredient, Dosage_Form) VALUES ({}, '{}', '{}', '{}')"
prescription_insert = "INSERT INTO Prescription (ID_Prescription, ID_Doctor, ID_Patient, Date_Prescribed) VALUES ({}, {}, {}, TO_DATE('2024-03-07', 'YYYY-MM-DD'))"
prescriptionDetail_insert = "INSERT INTO Prescription_Details (ID_Detail, ID_Prescription, ID_Medication, Times_Per_Day, Dose) VALUES ({}, {}, {}, '{}', '{}')"


insert_statements = []

for i, patient_id in enumerate(patients_ids):
    insert_statements.append(patient_insert.format(patient_id, *patients[i]))

for i, doctor_id in enumerate(doctors_ids):
    insert_statements.append(doctor_insert.format(doctor_id, *doctors[i]))

for i, medication_id in enumerate(medicines_ids):
    insert_statements.append(medicine_insert.format(medication_id, *medicines[i]))

for i in range(5):
    prescription_id = prescriptions_ids[i]
    insert_statements.append(prescription_insert.format(prescription_id, doctor_id, patients_ids[i]))

    for j in range (1):
        detail_id = generate_random_number()
        medIndex = i * 1 + j
        if medIndex < len(medicines_ids):
            medication_id = medicines_ids[medIndex]
            times_per_day = 3 if j % 2 == 0 else 2
            dose = 1 if j % 2 == 0 else 2
            insert_statements.append(prescriptionDetail_insert.format(detail_id, prescription_id, medication_id, times_per_day, dose))


for statement in insert_statements:
    cursor.execute(statement)

connection.commit()


