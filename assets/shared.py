import base64

PREDEFINED_QUESTIONS = [
    "👩‍💻 What is Janneke's current role?",
    "💼 What are Janneke's top skills?",
    "💪 What are Janneke's strengths?",
    "🎯 What are Janneke's key accomplishments?",
    "📈 How has Janneke contributed to the growth of previous organizations?",
    "🏆 What awards or recognitions has Janneke received?",
    "🌍 What industries or sectors has Janneke worked in?",
    "📚 What is Janneke's educational background?",
    "🤝 How does Janneke collaborate with team members?",
    "🔧 What tools and technologies is Janneke proficient in?"
]

RESUME_TEXT = """
Name: Janneke Clever
Location: Johns Island in Charleston, SC area (Originally from Myrtle Beach, SC)
Phone: 843.467.1821
Email: jannekemorin@gmail.com
LinkedIn: linkedin.com/in/jannekeclever

EXPERIENCE
Title: Technical Consultant II
Company: Capgemini Government Solutions
Date Range: Feb 2024 - Present
- Developed a scalable Generative AI prototype on AWS to transform information retrieval and response generation.
- Modernized a legacy R-based classification model using Azure ML, improving transparency and efficiency.
- Optimized key report generation by automating data prep steps, achieving a 75% reduction in manual effort.
- Delivered SharePoint form and setup redesign, meeting client needs and optimizing user experience.
- Created a central AI knowledge base, driving ethical standards across projects, training, and go-to-market.

Title: Technical Consultant I
Company: Capgemini Government Solutions
Date Range: Jan 2022 - Jan 2024
- Spearheaded development of a Power BI-based zip code lookup tool, enabling seamless program referrals nationwide.
- Improved data accuracy and compliance by implementing Azure AI-driven form processing and correction.
- Led a company-wide hackathon, fostering employee upskilling in AI and sustainability initiatives.
- Supported AI-related proposal bids by collecting qualifications and structuring key data.

Title: Technical Operations Specialist
Company: Ceterus
Date Range: May 2020 - Sep 2021
- Managed and responded to hundreds of complex product support tickets.
- Accurately documented and escalated technical issues to the Software Engineering Team.
- Utilized technologies such as SQL, Curl, and Google Data Studio to analyze information for ad hoc requests.
- Revamped technical processes for improved efficiency while clearly documenting new procedures.

Title: RISE Leadership Program
Company: Capgemini
Date Range: Aug 2021
- Built an interactive tech solution focused on improving employee engagement for a manufacturing company.

Title: Computer Science Tutor
Company: College of Charleston
Date Range: Aug 2019 - Dec 2019
- Tutored peers in Computer Science and Data Science courses at the Center for Student Learning.

EDUCATION
Degree: Bachelor of Science (BS) in Computer Science
School: College of Charleston
Graduation Date: Fall 2021
- Minor: Data Science
- Cyber Security Club: Member
- Honors College
- GPA: 3.98

SKILLS
- Programming Languages: Java, Python, R, C, SQL, JavaScript, HTML, CSS (10,000+ lines written)
- Experience: 5+ years in AI/ML, Analytics, Data Modeling, Data Visualization
- Tools: Proficient in Azure & AWS Cloud Platforms, Power BI, Power Apps

AWARDS
- School of Science and Mathematics Research Grant Recipient - CofC, Summer 2019
- Richard Crosby Award for highest achievement in CSCI 220 (introductory CS class) - CofC, Spring 2019
- First Year Writing Award - CofC, Spring 2019

VOLUNTEER EXPERIENCE
Title: Student Mentor
Organization: INTelligence Elementary School Program
Date Range: Jan 2020 - Mar 2020
- Worked with peers to introduce coding concepts to local elementary school students.

PERSONAL INFORMATION
- Married and residing in Johns Island.
- Running: Enjoy participating in local races and maintaining an active lifestyle.
- Cooking: Passionate about experimenting with new recipes and cuisines.
- Dog Lover: Loves dogs
"""

CUSTOM_BUTTON_MD = """
<style>
div.stButton > button:first-child {
    font-size: 1em; /* Use em for relative font size */
    padding: 1em; /* Use em for relative padding */
    color: #333; /* Dark text color */
    background-color: #f9f9f9; /* Light grey background */
    border: 1px solid #ddd; /* Slightly darker grey border */
    border-radius: 8px; /* Rounded edges */
    text-align: left; /* Left align the text */
    display: block;
    width: 100%; /* Full width inside column */
    margin: 10px 0;
    cursor: pointer;
    transition-duration: 0.3s;
    height: auto; /* Allow height to adjust automatically */
    min-height: 120px; /* Set a minimum height */
}
div.stButton > button:first-child:hover {
    background-color: #e0e0e0;
    border-color: #ccc;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow on hover */
}
</style>
"""
GEMINI_FLASH_MODELS = ["gemini-1.5-flash-exp-0827", "gemini-1.5-flash", "gemini-1.5-flash-002", "gemini-1.5-flash-8b", "gemini-1.5-flash-8b-exp-0924"]
GEMINI_PRO_MODELS = ["gemini-1.5-pro-002", "gemini-1.5-pro", "gemini-1.5-pro-exp-0827", "gemini-1.0-pro"]

MODEL_DICT = {
    "Gemini Flash - tasks requiring quick responses.":"Flash",
    "Gemini Pro - tasks requiring deep analysis and extended context.":"Pro"
}

# Function to encode an image to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()