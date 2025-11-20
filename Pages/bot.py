import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# --- 1. CONFIGURATION AND INITIALIZATION ---

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Set up Streamlit page (must be the first Streamlit command)
st.set_page_config(page_title="Medical AI Assistant", layout="centered")

# Inject custom CSS for the floating effect
def local_css(file_name):
    """Loads and applies custom CSS from a file."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: CSS file '{file_name}' not found. The chat window will not float.")

local_css("style.css") 

# Initialize Gemini Client
if "client" not in st.session_state:
    if not API_KEY:
        st.error("GEMINI_API_KEY not found. Please create a .env file and add your key.")
    else:
        st.session_state.client = genai.Client(api_key=API_KEY)
    
# System instruction to define the chatbot's persona
system_instruction = (
    "You are a professional, concise medical health assistant. "
    "Only respond to health and medical-related questions. "
    "If a question is unrelated, politely inform the user you can only answer medical queries."
    "Always include a strong disclaimer at the end of every response: 'Disclaimer: This is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.'"
)
config = types.GenerateContentConfig(
    system_instruction=system_instruction
)

# Initialize chat history (Streamlit session_state maintains it across reruns)
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": "Hello! I am your AI Medical Assistant. How can I assist you with your health-related questions today?"}
    )

# --- 2. GEMINI RESPONSE FUNCTION ---

def get_gemini_response(prompt):
    """Generates a response using the Gemini API, preserving chat history."""
    try:
        # Create a new chat session (or reuse if possible, but recreating here for simplicity with history)
        chat = st.session_state.client.chats.create(model="gemini-2.5-flash", config=config)
        
        # CORRECTED: Convert Streamlit history format to Gemini SDK Content format
        history = [
            types.Content(
                role="user" if msg["role"] == "user" else "model",
                # Use the explicit Part constructor to ensure correct formatting
                parts=[types.Part(text=msg["content"])] 
            ) 
            for msg in st.session_state.messages if msg["content"] # Ignore empty messages
        ]
        
        # The new prompt must be added to the contents array for the API to process it
        # Since we use a full-history approach, we pass the current prompt as part of the total history.
        
        # NOTE: For the `chats.create` method with history, you send the full conversation,
        # then use `send_message` with the next part. However, since Streamlit re-runs, 
        # a simpler method is to use `generate_content` and pass the full history plus the new prompt.
        # Let's adjust to use the `generate_content` approach for simpler history management in Streamlit:
        
        # The history list already contains all messages *before* the current user prompt.
        # Add the new user prompt as the final entry in the content list.
        current_contents = history + [types.Content(role="user", parts=[types.Part(text=prompt)])]
        
        response = st.session_state.client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=current_contents, 
            config=config
        )
        return response.text
        
    except Exception as e:
        return f"An error occurred with the API: {e}"

# --- 3. STREAMLIT UI DISPLAY AND INPUT ---

st.title("🩺 Medical AI Assistant")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if user_input := st.chat_input("Ask a medical question..."):
    # 1. Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Get and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing your query..."):
            assistant_response = get_gemini_response(user_input)
        st.markdown(assistant_response)
        
    # 3. Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})