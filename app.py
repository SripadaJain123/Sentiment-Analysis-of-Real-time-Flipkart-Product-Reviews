import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Flipkart Sentiment Analysis",
    page_icon="🛒",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    with open("sentiment_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# UI
st.title("🛒 Flipkart Review Sentiment Analysis")
st.write("Enter a product review to predict its sentiment")

# Input text
review = st.text_area("✍️ Enter Review", height=150)

# Predict button
if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review text")
    else:
        prediction = model.predict([review])[0]

        if prediction == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😡 Negative Review")
