import streamlit as st
st.set_page_config(page_title="Clinic System", layout="wide")
st.title("Clinic Management — Home")
st.write("""
Welcome — this Streamlit multi-page app includes:
- Patient management (add/view)
- Appointments, prescriptions, bills
- Disease diagnosis page with 100 symptom indicators and a bundled simple `model.pkl`
- AI medical chatbot demo page
""")
st.info("When you first run the app, a local SQLite database (`clinic.db`) will be created automatically in the app folder.")
