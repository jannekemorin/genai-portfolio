# 🎉 Streamlit Portfolio Powered by GenAI 🚀

Welcome to this **lightweight, interactive portfolio template** that showcases your GenAI skills! Users can ask questions about your resume using **Google Gemini**. Let's get started! 💻✨

---

## 🚀 Fork the Repository

1. Go to the repository on GitHub: `https://github.com/jannekemorin/genai-portfolio`.
2. Click the **Fork** button in the top-right corner of the page, leaving all settings as default, to create a copy of the repository under your GitHub account.
3. Open your terminal and navigate to the folder where you'd like to download your forked repository.
4. Run the following command to clone your forked repository (replace `<your-username>` with your GitHub username):

   ```bash
   git clone https://github.com/<your-username>/genai-portfolio
   ```

---

## 📦 Install Dependencies

After forking and cloning the repository, you need to install the required dependencies.

1. Navigate into the local repository:

   ```bash
   cd genai-portfolio
   ```

2. Install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   _💡 Note: Ensure that you have Python and `pip` installed on your system. You can check by running `python --version` and `pip --version`. 

---

## 🔍 Open the Repository

Ensure you have the forked repository open in your favorite code editor.

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

_💡 Troubleshooting: If you encounter an error while running the app, ensure all dependencies are installed and that your API key is correctly set up._

---

## 🛠 Customize Your Portfolio

Make it **yours** by updating these files:

### 📸 Assets

- **assets/Headshot.png**: Replace with a picture of yourself.
- **assets/Resume.pdf**: Upload a PDF version of your resume.
- **assets/Resume.txt**: Replace with plain text from your resume.

### 🗂 Configuration

- **config.py**:
  - Update the `FIRST_NAME` variable with your first name to personalize predefined questions.
  - Optionally, customize the predefined questions by editing the `PREDEFINED_QUESTIONS` list. You can add, remove, or modify questions to better reflect your experience and expertise.
  - Update the `LINKEDIN_LINK`, `EMAIL_LINK`, and `GITHUB_LINK` variables to reflect your accounts.
  - Adjust the `HOMEPAGE_TITLE`, `HOMEPAGE_SUBTITLE`, and `HOMEPAGE_BIO` to reflect your specialties.

- **.streamlit/config.toml**:
  - Optionally, customize the accent color for the application.

The **Home.py** and **pages/Q&A.py** files will pull from this file to customize the homepage and Q&A page, respectively.

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
5. Under **Advanced settings**, add this environment variable:

   ```bash
   API_KEY="YOUR_GEMINI_API_KEY"
   ```

6. Click **Deploy**.

_💡 Tip: Make sure all changes are pushed to GitHub before deploying._

---

## 🎉 Congratulations!

Your portfolio is now live and ready to be shared with the world! 🌍✨ Show off those GenAI skills and let users explore your resume interactively!

---

### 💡 Pro Tip: Keep Improving!

Feel free to continue customizing and improving this portfolio as you grow in your GenAI journey!