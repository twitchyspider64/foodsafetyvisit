import smtplib
from email.message import EmailMessage
import os

def get_recipient(data):
    if data["percentage"] < 85:
        return "ops@email.com"
    if data["restaurant_number"] == "2616":
        return "rothwell@email.com"
    return "admin@email.com"

def send_email(recipient, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Food Safety Audit Report"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = recipient
    msg.set_content("Attached is the audit report.")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
                           subtype="pdf", filename="audit.pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_USER"),
                     os.getenv("EMAIL_PASS"))
        server.send_message(msg)
