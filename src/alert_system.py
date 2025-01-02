# src/alert_system.py
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    """Send an alert email."""
    msg = MIMEText(message)
    msg['Subject'] = 'Security Alert'
    msg['From'] = 'security@yourdomain.com'
    msg['To'] = 'admin@yourdomain.com'

    with smtplib.SMTP('smtp.yourdomain.com') as server:
        server.login('user', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

send_alert("Suspicious login attempt detected!")