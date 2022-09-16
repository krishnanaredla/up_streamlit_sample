import streamlit as st
import pgeocode
import pandas as pd
import zipcodes

nomi = pgeocode.Nominatim("us")


with st.form("intake_form"):
    zip = st.number_input(
        label="What's your address or zip code? This question is required. *",
        min_value=10000,
        max_value=99999,
    )
    condition = st.multiselect(
        label="What condition are you interested in finding care for? This question is required. *",
        options=[
            "Polycystic Kidney Disease (PKD)",
            "Alport Syndrome",
            "Any rare Chronic Kidney Disease (CKD)",
        ],
    )
    care = st.multiselect(
        label="What types of care are the most inconvenient to access? This question is required. *",
        options=[
            "Nephrologist specializing in my condition",
            "CKD dietitian",
            "Clinical trial",
            "CKD support groups",
        ],
    )
    aspects = st.text_input(
        label="What are the most challenging aspects of getting quality care?"
    )
    email = st.text_input(
        label="If comfortable sharing, what's your email address?", value=""
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        if zipcodes.is_real(str(zip)):
            # st.write(int(zip))
            data = nomi.query_postal_code(int(zip))[["latitude", "longitude"]].to_dict()
            df = pd.DataFrame(data, index=[0])
            # st.write(df)
            st.map(df)
        else:
            st.write("Zip code is inavlid")
