# 🛒 Sentiment Analysis of Real-time Flipkart Product Reviews

This project is a **Sentiment Analysis Web Application** that predicts whether a user-provided Flipkart product review is **Positive or Negative** using Machine Learning and Natural Language Processing (NLP).

The application is built with **Streamlit** and deployed on **AWS EC2**.

---

## 🚀 Project Overview

- User enters a product review
- The trained ML model analyzes the sentiment
- The application displays the sentiment in real time

---

## 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorizer
- NLP (NLTK)
- AWS EC2

---

## 📂 Project Structure

Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/
│── app.py
│── sentiment_model.pkl
│── requirements.txt
│── README.md



---

## ⚙️ Machine Learning Model

- Text Preprocessing:
  - Lowercasing
  - Removing punctuation
  - Stopword removal
- Feature Extraction:
  - TF-IDF Vectorization
- Classification:
  - Machine Learning classifier trained on Flipkart reviews

---

## ▶️ Run the Application Locally

### Step 1: Install dependencies
```bash
pip install -r requirements.txt

Step 2: Run Streamlit app
python -m streamlit run app.py

Step 3: Open browser
http://localhost:8501
