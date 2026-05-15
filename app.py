import streamlit as st
import pickle
import re
import string

from nltk.corpus import stopwords

# LOAD MODEL
model = pickle.load(
    open("spam_classifier_model.pkl", "rb")
)

# LOAD TFIDF
tfidf = pickle.load(
    open("tfidf_vectorizer.pkl", "rb")
)

# STOPWORDS
stop_words = set(stopwords.words('english'))

# PREPROCESS FUNCTION
def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'\d+', '', text)

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# TITLE
st.title("📧 Email Spam Classifier")

# INPUT BOX
user_input = st.text_area(
    "Enter Email Message"
)

# PREDICT BUTTON
if st.button("Predict"):

    cleaned_input = preprocess_text(user_input)

    vector_input = tfidf.transform(
        [cleaned_input]
    )

    prediction = model.predict(
        vector_input
    )

    if prediction[0] == 1:
        st.error("Spam Email Detected")
    else:
        st.success("Ham Email")
