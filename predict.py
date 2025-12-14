import pickle

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

email = ["Congratulations! You won a free gift card"]
email_vec = vectorizer.transform(email)

prediction = model.predict(email_vec)
print("Spam" if prediction[0] == 1 else "Not Spam")
