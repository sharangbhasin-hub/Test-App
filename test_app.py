import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# IMPORTANT: Add your GOOGLE_API_KEY to your Streamlit secrets.
# Go to "Manage app" -> "Settings" -> "Secrets" and add:
# GOOGLE_API_KEY = "your_actual_api_key_here"

API_KEY = os.getenv("GOOGLE_API_KEY")

st.title("🧪 Gemini API Connection Test")

if not API_KEY:
    st.error("Error: GOOGLE_API_KEY is not set in your Streamlit secrets.")
else:
    try:
        # Configure the client with your API key
        genai.configure(api_key=API_KEY)
        
        st.success("✅ `genai.configure` executed successfully.")
        
        st.write("Attempting to list available models...")
        
        # List the available models
        models_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        st.success("✅ Successfully connected to the Google AI API and fetched models.")
        
        st.write("### Models that support `generateContent`:")
        st.write(models_list)

    except Exception as e:
        st.error(f"An error occurred during the test:")
        st.exception(e)
