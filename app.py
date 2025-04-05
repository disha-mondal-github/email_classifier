import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('email.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.set_page_config(page_title="Email Spam Classifier 📧", layout="centered")
st.title("📧 Spam or Ham Email Classifier")
st.write("Enter an email below and find out if it's **Spam (0)** or **Ham (1)**.")

# Text input from user
user_input = st.text_area("✉️ Enter Email Content Here:")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform input using the saved vectorizer
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            st.error("🚫 This email is classified as **Spam**.")
        else:
            st.success("✅ This email is classified as **Ham (Not Spam)**.")
