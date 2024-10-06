import google.generativeai as genai
import os
import sys
import streamlit as st
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.shared import *

# Configure the API key
genai.configure(api_key=os.environ["API_KEY"])

# Set session state variables
if "button_question" not in st.session_state:
    st.session_state.button_question = ""
if "custom_question" not in st.session_state:
    st.session_state.custom_question = ""
if "user_question" not in st.session_state:
    st.session_state.user_question = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "button_questions" not in st.session_state:
    st.session_state.button_questions = random.sample(PREDEFINED_QUESTIONS, 3)

# Create title
st.title("Resume Q&A")
st.info("Powered by Google Gemini Pro")
st.selectbox("Model", list(MODEL_DICT.keys()), key="selected_model")

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
        st.session_state.custom_question = ""  # Clear custom question
    else:
        st.session_state.user_question = st.session_state.custom_question
        st.session_state.button_question = ""  # Clear button question

    prompt = f"""
    As an advocate for the candidate, please focus exclusively on the following resume details:
    {RESUME_TEXT}

    Answer the question for potential recruiters, keeping the response professional, positive, and emphasizing the candidate's strengths, experiences, and suitability for the role.

    Please refrain from discussing any topics not directly related to the resume content. 
    For any questions not explicitly answered in the resume, please direct inquiries to the candidate's email: jannekemorin@gmail.com.

    Question: {st.session_state.user_question}
    """

    # Generate a response from the model
    model = genai.GenerativeModel(MODEL_DICT[st.session_state.selected_model])
    st.session_state.response = model.generate_content(prompt)

# Add three randomized questions to the columns
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
                              key="custom_question", 
                              on_change=send_prompt, 
                              args=(None, "input"))  # Use session state directly here

# Display the question and result only if there is a user question and a response
if st.session_state.user_question and st.session_state.response:
    st.divider()
    st.markdown(f"**{st.session_state.user_question}**")
    st.markdown(st.session_state.response.text)
