import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from backend.config import Config


def send_email(recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = Config.SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject

    body = MIMEText(message, 'plain')
    msg.attach(body)

    try:
        server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
        server.starttls()
        server.login(Config.SENDER_EMAIL, Config.SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(Config.SENDER_EMAIL, recipient_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
