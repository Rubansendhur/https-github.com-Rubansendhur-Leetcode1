SELECT patient_id, patient_name, conditions
FROM patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'
