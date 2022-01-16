import streamlit as st
import requests
import requests
import json

APPLICATION_SERVICE_URL = "http://application_layer:8000"

application_form = st.form(key="application-layer")
application_email = application_form.text_input("Enter your email")
application_password = application_form.text_input("Enter your password")
application_submit = application_form.form_submit_button("Submit")

st.title("Dummy secure application")


if application_submit:
    login_data = {"email": application_email, "password": application_password}
    r = requests.post(APPLICATION_SERVICE_URL + "/login", data=json.dumps(login_data))
    st.write(f"hello {r.text}")
