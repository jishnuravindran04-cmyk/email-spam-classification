📨 Email Spam Classification Using NLP and Machine Learning

Python • Streamlit • NLP • Machine Learning • Deep Learning

🎓 Course Details
Field	Details
Course	Predictive Analytics
Institution	Digital University Kerala
Instructor	Aswin S
Year	2025–2027
👥 Team Members
Name	GitHub
Anagha S	anaghasuresh0808
Meera G	meeraa77
Jishnu Ravindran	jishnuravindran04-cmyk
📌 Problem Statement

Email spam has become one of the major challenges in digital communication systems. Spam emails contain advertisements, phishing links, fraudulent content, and malicious attachments that can negatively impact users and organizations.

This project aims to build an automated Email Spam Classification system using Natural Language Processing (NLP) and Machine Learning techniques to accurately classify emails/messages as:

✅ Ham (Legitimate Email)
❌ Spam (Unwanted/Malicious Email)
💡 Motivation
Reduce unwanted spam emails
Improve digital communication security
Detect phishing and suspicious messages automatically
Apply NLP techniques on real-world text data
Compare Machine Learning and Deep Learning approaches for text classification
📦 Dataset
Property	Details
Dataset Name	email_dataset_classification.csv
Dataset Size	215,140 emails
Problem Type	Binary Classification
Target Labels	Spam / Ham
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
📂 Dataset Features
Feature	Description
Unnamed: 0	Index Column
message	Email text/message content
label	Target label (Spam/Ham)
Actual Useful Features
message
label
🔬 Methodology — Data Science Life Cycle
Stage 1: Problem Definition & Literature Review
Defined the task as binary text classification
Studied spam detection techniques using:
TF-IDF
Machine Learning classifiers
Deep Learning models
Compared traditional ML and LSTM approaches
Stage 2: Data Collection & Data Understanding
Loaded dataset from CSV file
Analysed:
dataset structure
missing values
class labels
feature types
Examined spam vs ham distribution
Stage 3: Data Preprocessing & Cleaning

Implemented preprocessing pipeline using NLP techniques:

Lowercasing text
Removing punctuation
Removing numbers
Stopword removal
Tokenization
Text normalization

Libraries used:

NLTK
Regex
Stage 4: Exploratory Data Analysis (EDA)

Performed visual analysis on dataset:

Spam vs Ham distribution
Word frequency analysis
Email/message length analysis
WordCloud visualization
Stage 5: Feature Engineering & Selection

Applied:

TF-IDF Vectorization

After preprocessing, email text was converted into numerical vectors using TF-IDF feature extraction for machine learning models.

Feature representation techniques used:

TF-IDF Vectorizer
Tokenization for LSTM sequences
Stage 6: Model Building & Training

Three models were implemented and compared:

Model	Technique
Naive Bayes (MultinomialNB)	TF-IDF
Support Vector Machine (LinearSVC)	TF-IDF
LSTM Neural Network	Word Embeddings
Stage 7: Model Evaluation & Comparison

Models were evaluated using:

Accuracy
F1 Score
Confusion Matrix
Classification Report
📊 Results Summary

| Model | Accuracy | Precision |
|---|---|
| Naive Bayes | 92.64% | 0.870 |
| SVM | 94.30% | 0.904 |
| LSTM | 96.10% | 0.95 |

✅ Best Model

The best-performing model was:

Support Vector Machine (SVM)
Why SVM Performed Best?
Highest Accuracy: 94.30%
Highest F1 Score: 0.904
Better spam detection capability
Balanced precision and recall performance
📈 Model Performance Visualizations
Confusion Matrix
Naive Bayes Confusion Matrix
SVM Confusion Matrix
LSTM Confusion Matrix
Additional Visualizations
WordCloud
Spam/Ham Distribution Graphs
Message Length Analysis
🖥️ Deployment

The project was deployed using Streamlit.

Features of the web application:

User-friendly interface
Real-time spam prediction
Text input for email/message classification
Displays prediction result instantly
🧠 Models Saved

The trained models and vectorizers were saved for deployment:

svm_model.pkl
naive_bayes_model.pkl
tfidf_vectorizer.pkl
tokenizer.pkl
🛠️ Technologies Used
Python
Scikit-learn
TensorFlow / Keras
TF-IDF Vectorizer
NLTK
Streamlit
Pandas
NumPy
Matplotlib
Seaborn
⚙️ Preprocessing Techniques
Lowercasing
Removing numbers
Removing punctuation
Stopword removal
Tokenization
TF-IDF feature extraction
📂 Project Structure
email-spam-classification/
│
├── dataset/
├── models/
├── notebooks/
├── images/
├── app.py
├── requirements.txt
├── README.md
└── presentation.pdf
🚀 Streamlit Deployment

Deployment Link:

Deployment in progress
📌 Future Work
Improve LSTM performance using larger embeddings
Implement BERT-based transformers
Add explainable AI techniques
Improve spam detection for multilingual emails
Deploy using cloud infrastructure
📖 Conclusion

This project successfully demonstrated how NLP and Machine Learning techniques can be used for email spam classification.

Among all models tested, SVM achieved the best performance with high accuracy and F1-score, making it the most effective model for deployment.

The project also provided hands-on experience in:

NLP preprocessing
Feature engineering
Machine Learning
Deep Learning
Model evaluation
Streamlit deployment
GitHub collaboration



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
