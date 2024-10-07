import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.shared import *

# Set page configuration
st.set_page_config(page_title="Home", layout="wide")

st.title("Hi, I'm Janneke Clever!")

# Create columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    # Introduction with emphasis
    st.markdown("### **Aspiring AI/ML Specialist**")
    st.markdown(
        f"""
        I am passionate about leveraging :red-background[technology] to solve real-world problems. 
        I enjoy exploring new :red-background[AI/ML] tools and techniques as well as collaborating with others on innovative projects.
        \n\nPlease check out my resume below or visit the Q&A tab to learn more!
        """
    )
    
    # Path to the local PDF file
    pdf_file_path = "./assets/Janneke's Resume.pdf"  # Replace with your local PDF path

    # Open the file in binary mode
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display download button with an icon (using emoji or text)
    st.download_button(
        label="📄 Download Resume",  # You can replace the emoji with text or another icon
        data=pdf_bytes,
        file_name="Janneke's Resume.pdf",  # Filename for the downloaded file
        mime="application/pdf"
    )
    
    if st.button("🗨️ Resume Q&A"):
        st.switch_page("pages/Q&A.py")

with col2:
    st.image("./assets/Graphic.png", width=350)  # Adjust width as needed

# Add sections with icons
col11, col12 = st.columns([1, 2])
with col11:
    st.divider()
    
    # Add links for LinkedIn and email with icons
    LI_icon = encode_image_to_base64("assets/LinkedIn.png")
    GH_icon = encode_image_to_base64("assets/GitHub.png")
    email_icon = encode_image_to_base64("assets/Email.png")
    st.markdown(
        f"""
        <h3>Let's Connect!</h3>
        <p style="margin-bottom: 15px;">
            <a href="https://www.linkedin.com/in/jannekeclever/" target="_blank" style="text-decoration: none; color: black;">
                <img src="data:image/png;base64,{LI_icon}" width="30" height="30" style="vertical-align: middle; margin-right: 8px;" />
                LinkedIn
            </a>
        </p>
        <p style="margin-bottom: 15px;">
            <a href="mailto:jannekemorin@gmail.com" style="text-decoration: none; color: black;">
                <img src="data:image/png;base64,{email_icon}" width="30" height="30" style="vertical-align: middle; margin-right: 8px;" />
                Email
            </a>
        </p>
        <p style="margin-bottom: 15px;">
            <a href="https://github.com/jannekemorin" style="text-decoration: none; color: black;">
                <img src="data:image/png;base64,{GH_icon}" width="30" height="30" style="vertical-align: middle; margin-right: 8px;" />
                GitHub
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )