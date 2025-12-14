from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        email = request.form["email"]
        email_vec = vectorizer.transform([email])
        prediction = model.predict(email_vec)
        result = "Spam Email 🚫" if prediction[0] == 1 else "Not Spam ✅"
    return f"""
        <h2>Spam Email Detection</h2>
        <form method="post">
            <textarea name="email" rows="6" cols="50"></textarea><br><br>
            <input type="submit" value="Check">
        </form>
        <h3>{result}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
