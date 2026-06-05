from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

# API key
API_KEY = os.getenv("BREVO_API_KEY")


def send_email(to_email, name):

    print(f"Sending email to {name} ({to_email})")

    # Demo message
    print("Email sent successfully\n")