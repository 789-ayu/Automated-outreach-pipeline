# Automated Outreach Pipeline

## About the Project

Automated Outreach Pipeline is a Python-based automation tool that helps discover similar companies, extract potential decision-makers from those companies, and send outreach emails through a simple command-line workflow.

The project follows a modular structure where each step, including company discovery, contact extraction, and email sending, is handled by a separate module.

## Features

- Discover companies similar to a given domain
- Extract decision-maker contacts (name, email) from target companies
- Review discovered contacts before sending emails
- Safety confirmation step before email execution
- Automated email outreach using API integration
- Secure API key management using environment variables

## Tech Stack

- **Python** – Core application logic and automation
- **python-dotenv** – Secure environment variable management
- **REST APIs**
  - Ocean.io – Company discovery
  - Prospeo – People/contact discovery
  - Brevo – Email sending automation

## How It Works

1. User enters a company domain.
2. `ocean.py` discovers similar companies related to the given domain.
3. `prospeo.py` extracts potential contacts from those companies.
4. The pipeline displays all discovered contacts with summary details.
5. User reviews the contacts and confirms whether to proceed.
6. `brevo.py` sends outreach emails after confirmation.

## Project Structure

```text
Automated-Outreach-Pipeline/
│
├── main.py          # Entry point - controls the complete workflow
├── ocean.py         # Company discovery module
├── prospeo.py       # Contact extraction module
├── brevo.py        # Email outreach module
├── .env            # API keys (not uploaded to GitHub)
├── .gitignore      # Ignored files configuration
└── README.md       # Project documentation
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
OCEAN_API_KEY=your_ocean_api_key
PROSPEO_API_KEY=your_prospeo_api_key
BREVO_API_KEY=your_brevo_api_key
```

### 4. Run the Application

```bash
python main.py
```

Enter a company domain, review the discovered contacts, and confirm whether to send outreach emails.

## Future Improvements

- Replace mock/demo data with live API responses
- Add a Streamlit-based graphical user interface
- Add personalized email templates
- Maintain outreach history to prevent duplicate emails
- Improve error handling for failed API requests

## Learning Outcomes

Through this project, I learned:

- How to structure a modular Python application
- How to securely manage API keys using environment variables
- How to design an automated workflow pipeline
- How to implement safety checks before executing important actions
- How to integrate multiple third-party APIs into a single application
