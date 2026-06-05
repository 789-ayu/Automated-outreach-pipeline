from ocean import get_similar_companies
from prospeo import get_people
from brevo import send_email


# User input
domain = input("Enter company domain: ")


# Get companies
companies = get_similar_companies(domain)

all_people = []


# Loop through companies
for company in companies:

    people = get_people(company)

    for person in people:

        print(person["name"])
        print(person["email"])
        print()

        all_people.append(person)


# Summary
print("Summary")
print(f"Total contacts found: {len(all_people)}")


# Safety confirmation
confirm = input("Send emails? (yes/no): ")


if confirm == "yes":

    for person in all_people:

        send_email(
            person["email"],
            person["name"]
        )

else:

    print("Email sending cancelled")