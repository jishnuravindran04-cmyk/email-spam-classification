# email-spam-classification
 This project classifies email/messages as Spam or Ham using Natural Language Processing (NLP), TF-IDF vectorization, and Machine Learning models. The final model was deployed as an interactive Streamlit web application for real-time predictions.


## Project Overview

This project detects whether an email/message is spam or ham using Natural Language Processing (NLP) techniques and Machine Learning algorithms.

The workflow includes:
- Data preprocessing
- Text cleaning
- Exploratory Data Analysis (EDA)
- Feature extraction using NLP
- Model training and evaluation

---

## Dataset

Dataset is too large for GitHub upload.

Download here:
https://drive.google.com/file/d/1_9iB0pZksEYLIxg4hdmD3jWpBN6xfJMs/view?usp=sharing



## Features

- Text preprocessing
- Stopword removal
- Tokenization
- Data visualization
- Spam/Ham classification
- Machine Learning model building


## Tech Stack

- Python
- Scikit-learn
- NLP
- TF-IDF Vectorization
- Streamlit
- Pandas
- NumPy
- NLTK


## Streamlit Application

The trained spam classification model was deployed using Streamlit for interactive real-time prediction.

### Features

- Real-time spam prediction
- Text preprocessing pipeline
- TF-IDF vectorization
- Clean user interface


## Text Preprocessing Pipeline

The input text undergoes several NLP preprocessing steps before prediction:

1. Convert text to lowercase
2. Remove numbers
3. Remove punctuation
4. Remove stopwords
5. Transform text using TF-IDF vectorization
