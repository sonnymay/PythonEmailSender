import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"  # Change this if using a different email provider
        smtp_port = 587  # Change this if using a different email provider

        # Create a secure connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create a multipart message
        email_message = MIMEMultipart()
        email_message["From"] = sender_email
        email_message["To"] = receiver_email
        email_message["Subject"] = subject

        # Attach the message to the email
        email_message.attach(MIMEText(message, "plain"))

        # Send the email
        server.send_message(email_message)
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

    finally:
        # Close the SMTP server connection
        server.quit()

# Example usage
sender_email = "your_email@gmail.com"  # Enter your email address
sender_password = "your_password"  # Enter your email password
receiver_email = "receiver_email@gmail.com"  # Enter the recipient's email address
subject = "Hello from Python!"
message = "This is a test email sent from a Python script."

send_email(sender_email, sender_password, receiver_email, subject, message)
