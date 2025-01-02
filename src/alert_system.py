import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(to_email, subject, message):
    """
    Sends an email alert with the provided subject and message.
    """
    from_email = 'your_email@example.com'
    password = 'your_email_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    body = MIMEText(message, 'plain')
    msg.attach(body)

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Alert sent to {to_email}")
    except Exception as e:
        print(f"Failed to send alert: {str(e)}")