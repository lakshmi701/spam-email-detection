📧 Spam Email Detection System (Machine Learning)
📌 Project Overview

The Spam Email Detection System is a machine learning–based application that automatically classifies emails as Spam or Not Spam.
It uses Natural Language Processing (NLP) techniques to analyze email text and predict whether an email is malicious or safe.

This project demonstrates end-to-end ML workflow including data preprocessing, feature extraction, model training, evaluation, and real-time prediction.

🎯 Objectives

Detect spam emails accurately

Learn text preprocessing & NLP techniques

Build and deploy a machine learning model

Create a resume-ready ML project

🧠 Technologies Used

Programming Language: Python

Libraries:

Pandas

NumPy

Scikit-learn

Pickle

Flask (optional web deployment)

ML Algorithm: Multinomial Naive Bayes

Feature Extraction: TF-IDF Vectorizer

📂 Project Structure
spam-email-detection/
│
├── dataset/
│   └── spam.csv
│
├── train_model.py        # Trains the ML model
├── predict.py            # Predicts spam/non-spam for input text
│
├── spam_model.pkl        # Saved trained model
├── vectorizer.pkl        # Saved TF-IDF vectorizer
│
├── app.py                # Flask web application
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation

📊 Dataset

Source: Kaggle (Spam Email Dataset)

Contains labeled emails:

0 → Not Spam

1 → Spam

⚙️ How the System Works

Load and clean the dataset

Convert text into numerical features using TF-IDF

Train a Naive Bayes classifier

Evaluate the model using accuracy and classification report

Save trained model and vectorizer

Predict spam emails in real-time

🚀 How to Run the Project
🔹 1. Install Dependencies
pip install -r requirements.txt

🔹 2. Train the Model
python train_model.py

🔹 3. Run Prediction (CLI)
python predict.py

🔹 4. Run Web Application
python app.py


Open browser:

http://127.0.0.1:5000/

📈 Model Performance

Accuracy: ~96.8%

High precision and recall for spam detection

🧪 Sample Output
Input: "Congratulations! You won a free prize"
Prediction: Spam

🔮 Future Enhancements

Improve accuracy using Logistic Regression or SVM

Add email file upload feature

Deploy on cloud (Heroku / Render)

Create modern UI using HTML & CSS

👩‍💻 Author

V Lakshmi Prasanna
Machine Learning Enthusiast | Python Developer