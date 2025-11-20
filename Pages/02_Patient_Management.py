import streamlit as st
from database import create_patient, get_patients
st.title("Patient Management")
st.subheader("Add Patient")
with st.form("add_patient"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    contact = st.text_input("Contact Number")
    submitted = st.form_submit_button("Add Patient")
    if submitted:
        if name.strip()=="":
            st.warning("Name required")
        else:
            create_patient(name, age, gender, contact)
            st.success("Patient added")
st.subheader("View Patients")
patients = get_patients()
if patients:
    import pandas as pd
    df = pd.DataFrame(patients, columns=["ID","Name","Age","Gender","Contact"])
    st.dataframe(df)
else:
    st.write("No patients yet.")
