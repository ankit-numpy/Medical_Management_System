import sqlite3

# Use a file-based SQLite DB (e.g., 'clinic.db')
def connect_db():
    return sqlite3.connect('clinic.db')


def create_patient(name, age, gender, contact_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, age, gender, contact_number)
        VALUES (?, ?, ?, ?)
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
        VALUES (?, ?, ?)
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
        VALUES (?, ?, ?, ?)
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
        VALUES (?, ?, ?)
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
    return bills


def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None
