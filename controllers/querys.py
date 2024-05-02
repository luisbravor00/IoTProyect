prescription_by_id = """
        SELECT
            Patients.Name AS Patient_Name,
            Patients.Last_name AS Patient_Last_name,
            Patients.Address AS Patient_Address,
            Patients.Age AS Patient_Age,
            Patients.Phone AS Patient_Phone,
            Patients.Email AS Patient_Email,
            Doctors.Name AS Doctor_Name,
            Doctors.Last_name AS Doctor_Last_name,
            Doctors.Phone_num AS Doctor_Phone,
            Doctors.Office_add AS Doctor_Address,
            Prescription.ID_Prescription,
            Prescription.Date_prescribed,
            Medicine.Name AS Medication_Name,
            Medicine.Active_Ingredient AS Medication_Active_Ingredient,
            Prescription_Details.DOSE,
            Prescription_Details.TIMES_PER_DAY
        FROM
            Prescription
        INNER JOIN
            Patients ON Prescription.ID_Patient = Patients.ID_Patient
        INNER JOIN
            Doctors ON Prescription.ID_Doctor = Doctors.ID_Doctor
        INNER JOIN
            Prescription_Details ON Prescription.ID_Prescription = Prescription_Details.ID_Prescription
        INNER JOIN
            Medicine ON Prescription_Details.ID_Medication = Medicine.ID_Medication
        WHERE
            Patients.ID_Patient = :id_patient
    """