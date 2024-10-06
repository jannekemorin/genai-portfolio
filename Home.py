import streamlit as st

# Set page configuration
st.set_page_config(page_title="Janneke Clever", layout="wide")

st.title("Hi, I'm Janneke Clever!")

# Create columns for layout
col1, col2 = st.columns([4, 8])

with col1:
    # Introduction with emphasis
    st.markdown("### I am a **young professional with a strong interest in AI/ML.**")
    st.markdown(
        """
        Passionate about leveraging technology to solve real-world problems. 
        I enjoy exploring new AI/ML techniques and collaborating on innovative projects.
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
    st.divider()
    # Add links for LinkedIn and email with icons
    st.markdown(
        """
        <h3>Connect with me:</h3>
        <p style="margin-bottom: 10px;">
            <a href="https://www.linkedin.com/in/jannekeclever/" target="_blank" style="text-decoration: none; color: black;">
                <img src="assets/LinkedIn.png" width="25" height="25" style="vertical-align: middle;" />
                LinkedIn
            </a>
        </p>
        <p>
            <a href="mailto:jannekemorin@gmail.com" style="text-decoration: none; color: black;">
                <img src="assets/Email.png" width="25" height="25" style="vertical-align: middle;" />
                Email
            </a>
        </p>
        <p>
            <a href="https://github.com/jannekemorin" style="text-decoration: none; color: black;">
                <img src="assets/GitHub.png" width="25" height="25" style="vertical-align: middle;" />
                Email
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    # Display image with adjusted size
    st.image("./assets/Graphic.png", width=500)  # Adjust width as needed