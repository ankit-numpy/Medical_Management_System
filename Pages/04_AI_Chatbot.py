import streamlit as st
st.title("AI Medical Chatbot")
st.write("You can enter a Gemini API key to use Google Gemini (if available). Otherwise the app will use a simple local rule-based responder (for demo only).")
api_key = st.text_input("Gemini API Key (optional)", type="password")
user_q = st.text_area("Describe symptoms or ask a medical question:")

def local_bot(q):
    ql = q.lower()
    if "fever" in ql:
        return "Fever noted — check temperature and stay hydrated. If >38°C, consult doctor."
    if "cough" in ql:
        return "Cough — consider whether it's dry/productive. If breathing difficulty, seek care."
    if "headache" in ql:
        return "Headache — rest, hydration, and OTC pain relief may help. If severe or persistent, see doctor."
    return "I can provide general guidance — for specific diagnosis, use the Diagnosis page or consult a physician."

if st.button("Ask"):
    if not user_q.strip():
        st.warning("Please enter a question or symptoms.")
    else:
        if api_key.strip():
            st.info("Gemini integration placeholder: add your integration in `pages/04_AI_Chatbot.py` to call the external API.")
            st.write(local_bot(user_q))
        else:
            st.write(local_bot(user_q))
