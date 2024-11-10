# 🎉 Streamlit Portfolio Powered by GenAI 🚀

Welcome to this **lightweight, interactive portfolio template** that showcases your GenAI skills! Users can ask questions about your resume using **Google Gemini**. Let's get started! 💻✨

---

## 🚀 Clone the Repository

1. Open your terminal and navigate to the folder where you'd like to download the repository.
2. Run the following command to clone the repository:

```bash
git clone https://github.com/jannekemorin/genai-portfolio
```

---

## 📦 Install Dependencies

After cloning the repository, you need to install the required dependencies.

1. Navigate into the cloned repository:

```bash
cd genai-portfolio
```

2. Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🔍 Open the Repository

Open the cloned repository in your favorite code editor.

---

## 🔑 Add Your Gemini API Key

1. [Get a free Gemini API Key from Google AI Studio](https://aistudio.google.com/app/apikey).
2. Inside the **.streamlit** folder, create a file named `secrets.toml`.
3. Add the following line to the file, replacing `YOUR_GEMINI_API_KEY` with your actual API key:

```toml
API_KEY="YOUR_GEMINI_API_KEY"
```

---

## ▶️ Run the Application

As you customize your portfolio, you can run it locally to preview changes.

1. In your terminal, navigate to the repository directory.
2. Run this command:

```bash
streamlit run Home.py
```

3. If successful, you'll see a message like this:

```bash
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://10.0.0.47:8501
```

4. Open the local URL in your browser to view your portfolio! 🌐🎉

---

## 🛠 Customize Your Portfolio

Make it **yours** by updating these files:

### 📸 Assets

- **assets/Headshot.png**: Replace with a picture of yourself.
- **assets/Resume.pdf**: Upload a PDF version of your resume.
- **assets/Resume.txt**: Replace with plain text from your resume.

### 🏠 Homepage Content

- **Home.py**:
  - Adjust the title and markdown text with your personal details.
  - Update the LINKEDIN_LINK, EMAIL_LINK, and GITHUB_LINK variables to reflect your accounts.

### ❓ Q&A Page Content

- **Q&A.py**:
  - Update the FIRST_NAME variable with your first name to personalize predefined questions.
  - Optionally, customize the predefined questions by editing the PREDEFINED_QUESTIONS list. You can add, remove, or modify questions to better reflect your experience and expertise.

---

## 🚀 Publish Your Repository on GitHub

1. In your terminal, while inside the repository directory, run these commands:

```bash
# Remove original remote URL
git remote remove origin

# Add YOUR GitHub repository as the new remote URL (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/genai-portfolio.git

# Push changes to your new GitHub repository
git push -u origin master
```

---

## 🌍 Deploy Your Portfolio on Streamlit

Streamlit makes it easy to share your app with others! Follow these steps:

1. Go to [Streamlit](https://streamlit.io/) and sign up for an account if you don’t have one already.
2. Link your GitHub account.
3. Head over to [Streamlit Share](https://share.streamlit.io/) and click **Create app**.
4. Fill out the following details:
   - **Repository**: `YOUR-USERNAME/genai-portfolio`
   - **Branch**: `main`
   - **Main file path**: `Home.py`
   - **App URL**: Choose a fun name! 🎨
5. Under **Advanced settings**, add this line:

```bash
API_KEY="YOUR_GEMINI_API_KEY"
```

6. Click **Deploy**.

---

## 🎉 Congratulations!

Your portfolio is now live and ready to be shared with the world! 🌍✨ Show off those GenAI skills and let users explore your resume interactively!

---

### 💡 Pro Tip: Keep Improving!

Feel free to continue customizing and improving this portfolio as you grow in your GenAI journey!