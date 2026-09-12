# 🤖 AI Resume Copilot

An AI-powered resume analysis and career guidance web application that helps users understand their skills, identify skill gaps, and prepare for their target job roles.

## 🚀 Features

* 📄 **Resume Analysis:** Upload resumes in PDF or DOCX format.
* 🎯 **Skill Gap Analysis:** Identify missing skills based on your desired job role.
* 🗺️ **Career Roadmap:** Get a personalized learning roadmap to improve your skills.
* 💬 **Interview Preparation:** Generate relevant interview questions for your target role.
* 🔐 **User Authentication:** Secure signup and login functionality.
* 📚 **Analysis History:** Save and review previous resume analysis reports.
* 🌐 **Web-Based Interface:** Simple and user-friendly dashboard.

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Database:** SQLAlchemy, SQLite/MySQL
* **Frontend:** HTML, CSS, JavaScript
* **AI & NLP:** AI-based resume analysis
* **File Processing:** PyPDF2, python-docx

## 📂 Project Structure

```text
AI Resume Copilot/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Resume-Copilot.git
cd AI-Resume-Copilot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and add your required AI API key and database configuration.

> Never upload API keys, passwords, or other sensitive credentials to GitHub.

### 6. Run the application

```bash
python app.py
```

Open the application at:

```text
http://127.0.0.1:5000
```

## 🔄 How It Works

1. Create an account or log in.
2. Upload your resume in PDF or DOCX format.
3. Enter your desired job role.
4. Submit your resume for analysis.
5. Review your skills, missing skills, career roadmap, and interview questions.
6. Access previous reports through the history section.

## 🔮 Future Improvements

* ATS score calculation and optimization suggestions.
* Resume keyword matching with job descriptions.
* Downloadable resume analysis reports.
* Improved AI recommendations.
* Resume builder and job application tracking.

## 👨‍💻 Author

**Divyansh Dubey**

BTech Computer Science Student | Aspiring Software Developer

## ⭐ Contributing

Contributions, suggestions, and feedback are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is intended for educational and personal portfolio purposes.
