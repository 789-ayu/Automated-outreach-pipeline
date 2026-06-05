from dotenv import load_dotenv
import os

# .env file load karega
load_dotenv()

# API key .env se lega
API_KEY = os.getenv("OCEAN_API_KEY")


def get_similar_companies(domain):

    print("\nFinding similar companies...\n")

    # Abhi testing ke liye mock data use kar rahe hain
    companies = [
        "slack.com",
        "notion.so",
        "zapier.com"
    ]

    return companies