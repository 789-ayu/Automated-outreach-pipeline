from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

# API key
API_KEY = os.getenv("PROSPEO_API_KEY")


def get_people(domain):

    print(f"Finding people from {domain}...\n")

    # Temporary demo data
    people = [
        {
            "name": "John Doe",
            "email": "john@example.com"
        },
        {
            "name": "Sarah Smith",
            "email": "sarah@example.com"
        }
    ]

    return people