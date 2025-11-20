# Clinic Management Streamlit App — v2

Upgraded demo with advanced diagnosis UI and a rule-based model:

- Inputs: weight (kg), height (cm), temperature (°F), BP single numeric, skin dropdown, diabetic Yes/No
- Diseases predicted: Viral Fever, Common Cold, Flu, Hypertension, Hypotension, Diabetes, Skin Allergy
- Optional 100 symptom checklist
- Diagnoses saved to `clinic.db`

How to run:
pip install streamlit
streamlit run medical_app_v2/pages/01_Home.py
