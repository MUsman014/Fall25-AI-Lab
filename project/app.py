from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# -----------------------------
# Load Trained ML Model
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# Home - HTML Page
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
# Prediction API
# -----------------------------
@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json

    features = [
        data["leaf_color_score"],
        data["moisture_level"],
        data["temperature"],
        data["humidity"],
        data["soil_ph"],
        data["spotting_severity"],
        data["wilt_level"]
    ]

    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]

    return jsonify({"prediction": int(prediction)})


# -----------------------------
# Form Submission from HTML
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict_form():
    features = [
        float(request.form["leaf_color_score"]),
        float(request.form["moisture_level"]),
        float(request.form["temperature"]),
        float(request.form["humidity"]),
        float(request.form["soil_ph"]),
        float(request.form["spotting_severity"]),
        float(request.form["wilt_level"])
    ]

    pred = model.predict([features])[0]

    return render_template("index.html", result=pred)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
