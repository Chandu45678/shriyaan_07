import smtplib
from email.message import EmailMessage

# Create email
msg = EmailMessage()
msg['Subject'] = "⚠ Account Verification Required"
msg['From'] = "security@company.com"
msg['To'] = "user@example.com"

msg.set_content("""
Dear User,

We detected suspicious activity in your account.
Please verify your account immediately.

NOTE:
This is a phishing simulation email
created strictly for educational purposes.

Regards,
Cyber Security Team
""")

# Mailtrap SMTP details
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
SMTP_USER = "555f422c02c307"
SMTP_PASS = "83a8b8fb0ec7e2"

# Send email
with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.starttls()
    server.login("555f422c02c307","83a8b8fb0ec7e2" )
    server.send_message(msg)

print("✅ Phishing simulation email sent successfully!")
