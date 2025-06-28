import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg['Subject'] = '📬 Biz Intel Alert'
    msg['From'] = 'amanalimar1993@gmail.com'
    msg['To'] = 'amanalimr1993@gmail.com@'
    msg.set_content('New business data collected. Check dashboard.')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('amanalimar1993@gmail.com', 'cfod fmof ctvw rmsx')
            smtp.send_message(msg)
            print("✅ Email sent")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_email()