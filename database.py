import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',  
        password='102410',  
        database='schema' 
    )


def create_patient(name, age, gender, contact_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, age, gender, contact_number)
        VALUES (%s, %s, %s, %s)
    ''', (name, age, gender, contact_number))
    conn.commit()
    cursor.close()
    conn.close()

def get_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return patients


def create_appointment(patient_id, appointment_date, doctor_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (patient_id, appointment_date, doctor_name)
        VALUES (%s, %s, %s)
    ''', (patient_id, appointment_date, doctor_name))
    conn.commit()
    cursor.close()
    conn.close()

def get_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.id, p.name, a.appointment_date, a.doctor_name
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
    ''')
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return appointments


def create_prescription(patient_id, medication, dosage, instructions):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO prescriptions (patient_id, medication, dosage, instructions)
        VALUES (%s, %s, %s, %s)
    ''', (patient_id, medication, dosage, instructions))
    conn.commit()
    cursor.close()
    conn.close()

def get_prescriptions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, patient_id, medication, dosage, instructions FROM prescriptions
    ''')
    prescriptions = cursor.fetchall()
    cursor.close()
    conn.close()
    return prescriptions


def create_bill(patient_id, description, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bills (patient_id, description, amount)
        VALUES (%s, %s, %s)
    ''', (patient_id, description, amount))
    conn.commit()
    cursor.close()
    conn.close()

def get_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, patient_id, description, amount FROM bills
    ''')
    bills = cursor.fetchall()
    cursor.close()
    conn.close()
    return 
    
def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = %s AND password = %s
    ''', (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None
