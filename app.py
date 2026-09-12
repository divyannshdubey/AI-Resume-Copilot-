
from flask import Flask, request, redirect, session, render_template
from ai import analyze_resume
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json


app = Flask(__name__)
app.secret_key = "divyansh123"


Base.metadata.create_all(bind=engine)


# HOME
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.User).filter_by(email=email).first()

        if existing_user:
            db.close()
            return "User already exists"

        user = models.User(
            email=email,
            password=password
        )

        db.add(user)
        db.commit()
        db.close()

        return redirect("/login")

    db.close()
    return render_template("signup.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(
            email=email,
            password=password
        ).first()

        if user:
            session["user"] = user.email
            db.close()
            return redirect("/dashboard")
        else:
            db.close()
            return "Invalid Credentials"

    db.close()
    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":

        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")

        file = request.files.get("file")

        # FILE HANDLING
        if file and file.filename != "":

            if file.filename.lower().endswith(".pdf"):

                try:
                    pdf_reader = PyPDF2.PdfReader(file)

                    text = ""

                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""

                    resume_text = text

                except Exception as e:
                    result = {
                        "error": f"PDF error: {str(e)}"
                    }

            elif file.filename.lower().endswith(".docx"):

                try:
                    doc = docx.Document(file)

                    text = ""

                    for para in doc.paragraphs:
                        text += para.text + "\n"

                    resume_text = text

                except Exception as e:
                    result = {
                        "error": f"Docx error: {str(e)}"
                    }

            else:
                result = {
                    "error": "Only PDF and DOCX files are supported."
                }

        # ANALYZE RESUME
        if resume_text and user_goal and result is None:

            try:
                result = analyze_resume(
                    resume_text,
                    user_goal
                )

                # SAVE TO DATABASE
                db = SessionLocal()

                user = db.query(models.User).filter_by(
                    email=session["user"]
                ).first()

                report = models.Reports(
                    user_id=user.id,
                    resume_txt=resume_text,
                    result=json.dumps(result)
                )

                db.add(report)
                db.commit()
                db.close()

            except Exception as e:
                result = {
                    "error": f"AI error: {str(e)}"
                }

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result
    )


# HISTORY
@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login")

    db = SessionLocal()

    user = db.query(models.User).filter_by(
        email=session["user"]
    ).first()

    reports = db.query(models.Reports).filter_by(
        user_id=user.id
    ).all()

    parsed_reports = []

    for r in reports:

        try:
            report_result = json.loads(r.result)

        except:
            report_result = {}

        parsed_reports.append({
            "resume": r.resume_txt,
            "result": report_result
        })

    db.close()

    return render_template(
        "history.html",
        reports=parsed_reports
    )


# LOGOUT
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)

