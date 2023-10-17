import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email address and password
email = ...
password = ...

# Recipient and subject
recipient = ...
subject = 'You won 1,000,000 dollars'

# Email body
email_body = 'I am a Python Master'

# Configure the email message
msg = EmailMessage()
msg['from'] = email
msg['to'] = recipient
msg['subject'] = subject
msg.set_content(html.substitute(name='TinTin'), 'html')

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()

    print("Email sent successfully.")
except Exception as e:
    print("An error occurred while sending the email: ", str(e))
