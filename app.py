from flask import Flask, render_template, request
from models import db, AuditSubmission
from scoring import calculate_score
from pdf_generator import generate_pdf
from email_utils import send_email, get_recipient
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///audits.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():

    responses = {}
    for key in request.form:
        if key.startswith("FS"):
            responses[key] = request.form.get(key)

    achieved, total, percentage, result = calculate_score(responses)

    data = {
        "restaurant_number": request.form["restaurant_number"],
        "manager_name": request.form["manager_name"],
        "date": request.form["date"],
        "percentage": percentage,
        "result": result
    }

    pdf_path = f"audit_{data['restaurant_number']}.pdf"
    generate_pdf(data, pdf_path)

    recipient = get_recipient(data)
    send_email(recipient, pdf_path)

    submission = AuditSubmission(
        restaurant_number=data["restaurant_number"],
        manager_name=data["manager_name"],
        date=data["date"],
        percentage=percentage,
        result=result
    )

    db.session.add(submission)
    db.session.commit()

    return render_template("success.html", percentage=percentage)

@app.route("/submissions")
def submissions():
    audits = AuditSubmission.query.order_by(
        AuditSubmission.created_at.desc()).all()
    return render_template("submissions.html", audits=audits)

if __name__ == "__main__":
    app.run(debug=True)
