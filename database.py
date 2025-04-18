import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='102410',  # Replace with your MySQL password
        database='schema'  # Replace with your database name
    )
    return conn

def create_patient(name, age, gender, contact_info):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, age, gender, contact_info) VALUES (%s, %s, %s, %s)
    ''', (name, age, gender, contact_info))
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
        INSERT INTO appointments (patient_id, appointment_date, doctor_name) VALUES (%s, %s, %s)
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