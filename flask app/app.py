from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# TRAIN MODEL ON STARTUP (no pickle needed)
df = pd.read_csv("StudentsPerformance.csv")

le = LabelEncoder()
for col in ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]:
    df[col] = le.fit_transform(df[col])

X = df.drop(["math score"], axis=1)
y = df["math score"]

model = RandomForestRegressor()
model.fit(X, y)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    form = request.json

    input_data = pd.DataFrame([{
        "gender": form['gender'],
        "race/ethnicity": form['race'],
        "parental level of education": form['parent'],
        "lunch": form['lunch'],
        "test preparation course": form['prep'],
        "reading score": form['reading'],
        "writing score": form['writing']
    }])

    for col in ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]:
        input_data[col] = le.fit_transform(input_data[col])

    prediction = model.predict(input_data)[0]
    return jsonify({"prediction": round(prediction, 2)})


if __name__ == "__main__":
    app.run(debug=True)

