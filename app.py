import streamlit as st

from ocean import get_similar_companies
from prospeo import get_people
from brevo import send_email

st.title("Automated Outreach Pipeline")

domain = st.text_input("Enter company domain")


if st.button("Run Pipeline"):

    companies = get_similar_companies(domain)

    all_people = []

    for company in companies:

        st.subheader(company)

        people = get_people(company)

        for person in people:

            st.write(person["name"])
            st.write(person["email"])

            all_people.append(person)

    st.success(f"Total contacts found: {len(all_people)}")

    if st.button("Send Emails"):

        for person in all_people:

            send_email(
                person["email"],
                person["name"]
            )

        st.success("Emails sent successfully")