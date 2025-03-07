

import streamlit as st
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif (any(char.isdigit() for char in password) and 
          any(char.islower() for char in password) and 
          any(char.isupper() for char in password) and 
          any(char in string.punctuation for char in password)):
        return "Strong"
    else:
        return "Moderate"

st.title("Password Strength Meter")

password = st.text_input("Enter your password:", type="password")
password_strength = check_password_strength(password)

st.write(f"Password Strength: {password_strength}")

if 'password_history' not in st.session_state:
    st.session_state.password_history = []

if st.button("Save Password"):
    if password:
        st.session_state.password_history.append(password)
        st.success("Password saved!")

st.subheader("Password History")
for pwd in st.session_state.password_history:
    st.write(pwd)

if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"Generated Strong Password: {strong_password}")

st.write("This app is created by Mithu with ❤️")