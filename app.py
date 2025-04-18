import streamlit as st
from database import create_patient, get_patients, create_appointment, get_appointments
from datetime import datetime

st.title("Medical Management System")

menu = ["Add Patient", "View Patients", "Add Appointment", "View Appointments"]
choice = st.sidebar.selectbox("Select an option", menu)

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
        for patient in patients:
            st.write(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Gender: {patient[3]}, Contact: {patient[4]}")
    else:
        st.write("No patients found.")

elif choice == "Add Appointment":
    st.subheader("Add Appointment")
    patient_id = st.number_input("Patient ID", min_value=1)
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    doctor_name = st.text_input("Doctor Name")

    if st.button("Add Appointment"):
        # Combine date and time into a single datetime object
        appointment_datetime = datetime.combine(appointment_date, appointment_time)
        create_appointment(patient_id, appointment_datetime, doctor_name)
        st.success("Appointment added successfully!")

elif choice == "View Appointments":
    st.subheader("Appointment List")
    appointments = get_appointments()
    if appointments:
        for appointment in appointments:
            st.write(f"Appointment ID: {appointment[0]}, Patient Name: {appointment[1]}, "
                     f"Date: {appointment[2]}, Doctor: {appointment[3]}")
    else:
        st.write("No appointments found.")