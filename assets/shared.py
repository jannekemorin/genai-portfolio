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

Technical Consultant II
Capgemini Government Solutions
Feb 2024 - Present
- Developed a scalable Generative AI prototype on AWS to transform information retrieval and response generation.
- Modernized a legacy R-based classification model using Azure ML, improving transparency and efficiency.
- Optimized key report generation by automating data prep steps, achieving a 75% reduction in manual effort.
- Delivered SharePoint form and setup redesign, meeting client needs and optimizing user experience.
- Created a central AI knowledge base, driving ethical standards across projects, training, and go-to-market.

Technical Consultant I
Capgemini Government Solutions
Jan 2022 - Jan 2024
- Spearheaded development of a Power BI-based zip code lookup tool, enabling seamless program referrals nationwide.
- Improved data accuracy and compliance by implementing Azure AI-driven form processing and correction.
- Led a company-wide hackathon, fostering employee upskilling in AI and sustainability initiatives.
- Supported AI-related proposal bids by collecting qualifications and structuring key data.

Technical Operations Specialist
Ceterus
May 2020 - Sep 2021
- Managed and responded to hundreds of complex product support tickets.
- Accurately documented and escalated technical issues to the Software Engineering Team.
- Utilized technologies such as SQL, Curl, and Google Data Studio to analyze information for ad hoc requests.
- Revamped technical processes for improved efficiency while clearly documenting new procedures.

RISE Leadership Program
Capgemini
Aug 2021
- Built an interactive tech solution focused on improving employee engagement for a manufacturing company.

Computer Science Tutor
College of Charleston
Aug 2019 - Dec 2019
- Tutored peers in Computer Science and Data Science courses at the Center for Student Learning.

EDUCATION

Bachelor of Science (BS) in Computer Science
College of Charleston
Graduated: Fall 2021
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

Student Mentor
INTelligence Elementary School Program
Jan 2020 - Mar 2020
- Worked with peers to introduce coding concepts to local elementary school students.

PERSONAL INFORMATION

- Married and residing in Johns Island.
- Running: Enjoy participating in local races and maintaining an active lifestyle.
- Cooking: Passionate about experimenting with new recipes and cuisines.
- Dog Lover: Loves dogs
"""

CUSTOM_BUTTON_MD ="""
<style>
div.stButton > button:first-child {
    font-size: 18px;
    padding: 15px; /* Padding for button */
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
    height: 100px; /* Fixed height for all buttons */
}
div.stButton > button:first-child:hover {
    background-color: #e0e0e0;
    border-color: #ccc;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow on hover */
}
</style>
"""

MODEL_DICT = {
    "gemini-1.5-flash-exp-0827 - tasks requiring quick responses.":"gemini-1.5-flash-exp-0827",
    "gemini-1.5-pro-exp-0827 - tasks requiring deep analysis and extended context.":"gemini-1.5-pro-exp-0827"
}

# Function to encode an image to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()