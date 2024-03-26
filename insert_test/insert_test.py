import random

# Función para generar un número aleatorio de 8 dígitos
def generate_random_number():
    return random.randint(10000000, 99999999)

# Generamos listas de números aleatorios para pacientes, doctores, medicinas y prescripciones
patient_ids = [generate_random_number() for _ in range(5)]
doctor_ids = [generate_random_number() for _ in range(5)]
medication_ids = [generate_random_number() for _ in range(5)]
prescription_ids = [generate_random_number() for _ in range(5)]
prescriptionDetails_ids = [generate_random_number() for _ in range(5)]

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
    ('Azitrocin', 'Azitromicina', 1),
    ('Lipitor', 'Atorvastatina', 2),
    ('Zestril', 'Lisinopril', 1),
    ('Glucophage', 'Metformina', 2),
    ('Amoxil', 'Amoxicilina', 1)
]

prescriptionDetails = [
    (3, 1),
    (3, 2),
    (2, 1),
    (2, 2)
]


# Templates para los INSERT statements
patient_insert = "INSERT INTO Patients (ID_Patient, Name, Last_name, Address, Age, Phone, Email) VALUES ({}, '{}', '{}', '{}', {}, '{}', '{}')"
doctor_insert = "INSERT INTO Doctors (ID_Doctor, Name, Last_name, Phone_num, Office_add) VALUES ({}, '{}', '{}', '{}', '{}')"
medicine_insert = "INSERT INTO Medicine (ID_Medication, Name, Active_Ingredient, Dosage_Form) VALUES ({}, '{}', '{}', '{}')"
prescription_insert = "INSERT INTO Prescription (ID_Prescription, ID_Doctor, ID_Patient, Date_prescribed) VALUES ({}, {}, {}, TO_DATE('2024-03-07', 'YYYY-MM-DD'))"
prescription_detail_insert = "INSERT INTO Prescription_Details (ID_Detail, ID_Prescription, ID_Medication, Times_Per_Day, Dose) VALUES ({}, {}, {}, '{}', '{}')"

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
    insert_statements.append(prescription_insert.format(prescription_id, doctor_id, patient_ids[i]))

    for j in range(3):
        # Generar y añadir statement para detalle de prescripción
        detail_id = generate_random_number()
        medIndex = i * 3 + j
        if medIndex < len(medication_ids):
            # 3 means every 8 hours
            # 2 means every 12 hours
            #times_per_day = 3 if i == 0 else 3 if i == 1 else 2 if i == 2 else 2 if i == 3 else 3
            #dose = 1 if i == 0 or i == 2 else 2
            medication_id = medication_ids[medIndex]
            times_per_day = 3 if j % 2 == 0 else 2
            dose = 1 if j % 2 == 0 else 2
            insert_statements.append(prescription_detail_insert.format(detail_id, prescription_id, medication_id, times_per_day, dose))

