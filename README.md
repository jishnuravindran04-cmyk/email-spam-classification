# 📨 Email Spam Classification Using NLP and Machine Learning

A complete Natural Language Processing (NLP) project for detecting whether an email/message is **Spam** or **Ham** using Machine Learning and Deep Learning techniques.

---

## 🚀 Project Overview

Email spam detection is one of the most important applications of Natural Language Processing (NLP). Spam emails may contain advertisements, phishing links, malicious content, or fraudulent messages that can compromise user security.

This project builds an automated spam classification system capable of classifying emails/messages as:

- ✅ Ham (Legitimate Message)
- ❌ Spam (Unwanted/Malicious Message)

The project includes:
- NLP preprocessing
- Exploratory Data Analysis (EDA)
- TF-IDF feature extraction
- Machine Learning & Deep Learning models
- Streamlit deployment for real-time prediction

---

## ▶️ Run the Streamlit App

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the app:
   ```bash
   streamlit run app.py
   ```
3. Open the local URL shown in the terminal to use the email spam classifier.

---

## 🎓 Course Details

| Field | Details |
|---|---|
| Course | Predictive Analytics |
| Institution | Digital University Kerala |
| Instructor | Aswin S |
| Academic Year | 2025–2027 |

---

## 👥 Team Members

| Name | GitHub |
|---|---|
| Anagha S | anaghasuresh0808 |
| Meera G | meeraa77 |
| Jishnu Ravindran | jishnuravindran04-cmyk |

---

## 📌 Problem Statement

Spam emails have become a major challenge in digital communication systems. These emails often contain phishing attempts, scams, advertisements, or malicious attachments.

The objective of this project is to build an intelligent classification system using NLP and Machine Learning techniques to automatically detect spam emails accurately.

---

## 💡 Motivation

- Reduce unwanted spam emails
- Improve communication security
- Detect phishing and suspicious messages automatically
- Apply NLP techniques to real-world text data
- Compare Machine Learning and Deep Learning approaches

---

## 📦 Dataset Information

| Property | Details |
|---|---|
| Dataset Name | `email_dataset_classification.csv` |
| Dataset Size | 215,140 Emails |
| Problem Type | Binary Classification |
| Target Labels | Spam / Ham |

### Dataset Features

| Feature | Description |
|---|---|
| `message` | Email text/message content |
| `label` | Target label (Spam/Ham) |

### Dataset Link

Dataset is too large for GitHub upload.

📥 Download Dataset:  
https://drive.google.com/file/d/1_9iB0pZksEYLIxg4hdmD3jWpBN6xfJMs/view?usp=sharing

---

# 🔬 Methodology — Data Science Life Cycle

## Stage 1: Problem Definition & Literature Review

- Defined the task as binary text classification
- Studied spam detection techniques using:
  - TF-IDF
  - Machine Learning classifiers
  - Deep Learning models
- Compared traditional ML and LSTM approaches

---

## Stage 2: Data Collection & Understanding

Performed:
- Dataset loading
- Structure analysis
- Missing value analysis
- Label distribution analysis
- Feature type identification

---

## Stage 3: Data Preprocessing & Cleaning

Implemented NLP preprocessing pipeline:

- Lowercasing
- Removing punctuation
- Removing numbers
- Stopword removal
- Tokenization
- Text normalization

### Libraries Used
- NLTK
- Regex

---

## Stage 4: Exploratory Data Analysis (EDA)

Performed visual analysis using:
- Spam vs Ham distribution
- Word frequency analysis
- Message length analysis
- WordCloud visualization
- Correlation analysis

---

## Stage 5: Feature Engineering & Selection

Applied:

### TF-IDF Vectorization
Converted text data into numerical feature vectors for Machine Learning models.

### Sequence Tokenization
Used tokenized sequences for LSTM-based Deep Learning model.

---

## Stage 6: Model Building & Training

Implemented and compared three models:

| Model | Technique |
|---|---|
| Naive Bayes (MultinomialNB) | TF-IDF |
| Support Vector Machine (LinearSVC) | TF-IDF |
| LSTM Neural Network | Word Embeddings |

---

## Stage 7: Model Evaluation & Comparison

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# 📊 Results Summary

| Model | Accuracy | F1 Score |
|---|---|---|
| Naive Bayes | 92.64% | 0.870 |
| SVM | 94.30% | 0.904 |
| LSTM | 96.10% | 0.950 |

---

# ✅ Best Performing Model

## LSTM Neural Network

### Why LSTM Performed Best?

- Highest Accuracy: **96.10%**
- Highest F1 Score: **0.950**
- Better contextual understanding
- Improved spam detection performance

---

# 📈 Visualizations

The project includes multiple visualizations such as:

- Confusion Matrix
- Spam vs Ham Distribution
- WordCloud
- Message Length Analysis
- Feature Distribution Graphs
- Model Comparison Charts

---

# 🖥️ Streamlit Deployment

The final model was deployed using Streamlit for real-time spam prediction.

### Application Features

- User-friendly interface
- Real-time prediction
- Text preprocessing pipeline
- Instant classification results

---

## 🚀 Deployment Link

http://localhost:8501/





