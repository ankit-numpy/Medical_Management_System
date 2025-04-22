import streamlit as st
from datetime import datetime
from database import (
    create_patient, get_patients,
    create_appointment, get_appointments,
    create_prescription, get_prescriptions,
    create_bill, get_bills,
    login_user
)

# --- User Authentication ---
def login():
    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# --- App Layout ---
st.title("Medical Management System")

menu = [
    "Add Patient", "View Patients",
    "Add Appointment", "View Appointments",
    "Add Prescription", "View Prescriptions",
    "Add Bill", "View Bills"
]
choice = st.sidebar.selectbox("Select an option", menu)

# --- Patient Registration ---
if choice == "Add Patient":
    st.subheader("Add Patient")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact_number = st.text_input("Contact Number")
    if st.button("Add Patient"):
        create_patient(name, age, gender, contact_number)
        st.success("Patient added successfully!")

elif choice == "View Patients":
    st.subheader("Patient List")
    patients = get_patients()
    if patients:
        patient_data = [{
            "ID": p[0],
            "Name": p[1],
            "Age": p[2],
            "Gender": p[3],
            "Contact": p[4]
        } for p in patients]
        st.dataframe(patient_data)
    else:
        st.write("No patients found.")

# --- Appointments ---
elif choice == "Add Appointment":
    st.subheader("Add Appointment")
    patient_id = st.number_input("Patient ID", min_value=1)
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    doctor_name = st.text_input("Doctor Name")
    if st.button("Add Appointment"):
        appointment_datetime = datetime.combine(appointment_date, appointment_time)
        create_appointment(patient_id, appointment_datetime, doctor_name)
        st.success("Appointment added successfully!")

elif choice == "View Appointments":
    st.subheader("Appointment List")
    appointments = get_appointments()
    if appointments:
        appointment_data = [{
            "Appointment ID": a[0],
            "Patient": a[1],
            "Date": a[2],
            "Doctor": a[3]
        } for a in appointments]
        st.dataframe(appointment_data)
    else:
        st.write("No appointments found.")

# --- Prescriptions ---
elif choice == "Add Prescription":
    st.subheader("Add Prescription")
    patient_id = st.number_input("Patient ID", min_value=1)
    medication = st.text_area("Medication")
    dosage = st.text_input("Dosage")
    instructions = st.text_area("Instructions")
    if st.button("Add Prescription"):
        create_prescription(patient_id, medication, dosage, instructions)
        st.success("Prescription added!")

elif choice == "View Prescriptions":
    st.subheader("Prescription List")
    prescriptions = get_prescriptions()
    if prescriptions:
        prescription_data = [{
            "Prescription ID": p[0],
            "Patient ID": p[1],
            "Medication": p[2],
            "Dosage": p[3],
            "Instructions": p[4]
        } for p in prescriptions]
        st.dataframe(prescription_data)
    else:
        st.write("No prescriptions found.")

# --- Billing ---
elif choice == "Add Bill":
    st.subheader("Add Bill")
    patient_id = st.number_input("Patient ID", min_value=1)
    description = st.text_input("Description of Service")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Add Bill"):
        create_bill(patient_id, description, amount)
        st.success("Bill added!")

elif choice == "View Bills":
    st.subheader("Bill List")
    bills = get_bills()
    if bills:
        bill_data = [{
            "Bill ID": b[0],
            "Patient ID": b[1],
            "Service": b[2],
            "Amount (₹)": b[3]
        } for b in bills]
        st.dataframe(bill_data)
    else:
        st.write("No bills found.")
