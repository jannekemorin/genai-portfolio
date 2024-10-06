# Import packages
import google.generativeai as genai
import os
import streamlit as st
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.shared import *

# Configure the API key
genai.configure(api_key=st.secrets["API_KEY"])

# Set session state variables
if "custom_input" not in st.session_state:
    st.session_state.custom_input = ""
if "user_question" not in st.session_state:
    st.session_state.user_question = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "button_questions" not in st.session_state:
    st.session_state.button_questions = random.sample(PREDEFINED_QUESTIONS, 3)
if "recent_model" not in st.session_state:
    st.session_state.recent_model = ""

# Create title
st.title("Resume Q&A")
st.info("Powered by Google Gemini Pro")
st.radio("Select a model family", list(MODEL_DICT.keys()), key="selected_model")

# Custom CSS to style buttons like ChatGPT
st.markdown(
    CUSTOM_BUTTON_MD,
    unsafe_allow_html=True
)

# Create section for predefined questions
st.subheader("Get started")
st.markdown("Try a sample question or add your own below!")

# Function to call API based on question type
def send_prompt(input_question, question_type):
    if question_type == "button":
        st.session_state.user_question = input_question
    else:
        st.session_state.user_question = st.session_state.custom_input

    prompt = f"""
    As an advocate for the candidate, please focus exclusively on the following resume details:
    {RESUME_TEXT}

    Answer the question for potential recruiters, keeping the response professional, positive, and emphasizing the candidate's strengths, experiences, and suitability for the role.

    Please refrain from discussing any topics not directly related to the resume content. 
    For any questions not explicitly answered in the resume, please direct inquiries to the candidate's email: jannekemorin@gmail.com.

    Question: {st.session_state.user_question}
    """
    
    model_version = MODEL_DICT[st.session_state.selected_model]
    
    # Determine which list of models to use
    model_list = GEMINI_FLASH_MODELS if model_version == "Flash" else GEMINI_PRO_MODELS
    
    for model_name in model_list:
        try:
            # Initialize and use the generative model
            model = genai.GenerativeModel(model_name)
            st.session_state.response = model.generate_content(prompt)
            if st.session_state.response:  # Check if response is successful
                st.session_state.recent_model = model
                break  # Exit loop if successful
        except Exception as e:
            print(f"Error with model {model_name}: {e}")
    
    if not st.session_state.response:
        st.warning("Sorry, but it seems we've reached the chat limit for all models. Please try again later. We appreciate your understanding and patience!")

# Add three randomized questions columns
col1, col2, col3 = st.columns(3)
with col1:
    q1 = st.session_state.button_questions[0]
    st.button(q1, on_click=send_prompt, args=(q1, "button"), key="q1_button")

with col2:
    q2 = st.session_state.button_questions[1]
    st.button(q2, on_click=send_prompt, args=(q2, "button"), key="q2_button")

with col3:
    q3 = st.session_state.button_questions[2]
    st.button(q3, on_click=send_prompt, args=(q3, "button"), key="q3_button")

# Create a text input for custom questions
custom_input = st.text_input("Type your question here:", 
                              key="custom_input", 
                              on_change=send_prompt, 
                              args=(None, "input"))  # Use session state directly here

# Display the question and result only if there is a user question and a response
if st.session_state.user_question and st.session_state.response:
    st.divider()
    st.subheader(st.session_state.user_question)
    st.markdown(st.session_state.response.text)
    st.info(f"Model used: {(st.session_state.recent_model.model_name).split("models/")[-1]}")
