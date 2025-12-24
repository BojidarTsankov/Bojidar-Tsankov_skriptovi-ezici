import smtplib
from email.message import EmailMessage

sender_email = "moqt_email"
receiver_email = "vashiq_email"
password = "ixvr tylz wokp xuis"

smtp_server = "smtp.gmail.com"
port = 587

msg = EmailMessage()
msg['Subject'] = "zadacha"
msg['From'] = "moqt_email"
msg['To'] = "vashiq_email"
msg.set_content('''Dear gospodine,

Eve's cat has been arrested for

catnapping, cat burglary, and extortion.

Sincerely,

Bojidar Tsankov''')

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent!")
except Exception as e:
    print(f"Error: {e}")
