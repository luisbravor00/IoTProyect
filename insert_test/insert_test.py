import random

# Función para generar un número aleatorio de 8 dígitos
def generate_random_number():
    return random.randint(10000000, 99999999)

# Generamos listas de números aleatorios para pacientes, doctores, medicinas y prescripciones
patient_ids = [generate_random_number() for _ in range(5)]
doctor_ids = [generate_random_number() for _ in range(5)]
medication_ids = [generate_random_number() for _ in range(5)]
prescription_ids = [generate_random_number() for _ in range(5)]

# Datos ficticios para pacientes, doctores y medicinas
patients = [
    ('John', 'Doe', '123 Main St', 30, '123-456-7890', 'john.doe@example.com'),
    ('Jane', 'Smith', '456 Oak St', 25, '234-567-8901', 'jane.smith@example.com'),
    ('Jim', 'Brown', '789 Pine St', 40, '345-678-9012', 'jim.brown@example.com'),
    ('Emily', 'Jones', '321 Maple St', 22, '456-789-0123', 'emily.jones@example.com'),
    ('David', 'Wilson', '654 Elm St', 35, '567-890-1234', 'david.wilson@example.com')
]

doctors = [
    ('Alice', 'Green', '678-901-2345', '123 Center St'),
    ('Bob', 'White', '789-012-3456', '456 Grand Ave'),
    ('Charlie', 'Black', '890-123-4567', '789 West St'),
    ('Diana', 'Gray', '901-234-5678', '321 East St'),
    ('Evan', 'Brown', '012-345-6789', '654 South St')
]

medicines = [
    ('Azitrocin', 'Azitromicina', 'Pill'), 
    ('Lipitor', 'Atorvastatina', 'Capsule'),
    ('Zestril', 'Lisinopril', 'Pill'),
    ('Glucophage', 'Metformina', 'Tablet'),
    ('Amoxil', 'Amoxicilina', 'Capsule')
]

# Templates para los INSERT statements
patient_insert = "INSERT INTO Patients (ID_Patient, Name, Last_name, Address, Age, Phone, Email) VALUES ({}, '{}', '{}', '{}', {}, '{}', '{}')"
doctor_insert = "INSERT INTO Doctors (ID_Doctor, Name, Last_name, Phone_num, Office_add) VALUES ({}, '{}', '{}', '{}', '{}')"
medicine_insert = "INSERT INTO Medicine (ID_Medication, Name, Active_Ingredient, Dosage_Form) VALUES ({}, '{}', '{}', '{}')"
prescription_insert = "INSERT INTO Prescription (ID_Prescription, ID_Doctor, ID_Patient, Date_prescribed) VALUES ({}, {}, {}, TO_DATE('2024-03-07', 'YYYY-MM-DD'))"
prescription_detail_insert = "INSERT INTO Prescription_Details (ID_Detail, ID_Prescription, ID_Medication, Dose, Frequency) VALUES ({}, {}, {}, '{}', '{}')"

# Generar los INSERT statements
insert_statements = []

# Añadir statements para pacientes
for i, patient_id in enumerate(patient_ids):
    insert_statements.append(patient_insert.format(patient_id, *patients[i]))

# Añadir statements para doctores
for i, doctor_id in enumerate(doctor_ids):
    insert_statements.append(doctor_insert.format(doctor_id, *doctors[i]))

# Añadir statements para medicinas
for i, medication_id in enumerate(medication_ids):
    insert_statements.append(medicine_insert.format(medication_id, *medicines[i]))

# Añadir statements para prescripciones y detalles de prescripciones
for i in range(5):
    prescription_id = prescription_ids[i]
    insert_statements.append(prescription_insert.format(prescription_id, doctor_ids[i], patient_ids[i]))
    
    # Generar y añadir statement para detalle de prescripción
    detail_id = generate_random_number()
    dose = '1 pill' if i == 0 else '2 capsules' if i == 1 else '1 tablet' if i == 2 else '20ml' if i == 3 else '1 injection'
    frequency = 'Twice a day' if i == 0 else 'Once a day' if i == 1 else 'Three times a day' if i == 2 else 'Four times a day' if i == 3 else 'Once a week'
    insert_statements.append(prescription_detail_insert.format(detail_id, prescription_id, medication_ids[i], dose, frequency))
