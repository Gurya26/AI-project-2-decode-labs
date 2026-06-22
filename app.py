from flask import Flask, render_template, request, jsonify
import joblib

# ----------------------------
# Flask App
# ----------------------------

app = Flask(__name__)

# ----------------------------
# Load Trained Model
# ----------------------------

model = joblib.load("iris_model.pkl")

# ----------------------------
# Flower Information
# ----------------------------

flowers = {

    0: {
        "name": "Iris Setosa",
        "scientific": "Iris setosa",
        "description": "A small flower with short petals and broad sepals. It is the easiest Iris species to identify.",
        "image": "🌸"
    },

    1: {
        "name": "Iris Versicolor",
        "scientific": "Iris versicolor",
        "description": "A medium-sized Iris flower known for its beautiful violet-blue petals.",
        "image": "🌺"
    },

    2: {
        "name": "Iris Virginica",
        "scientific": "Iris virginica",
        "description": "The largest Iris species with long petals and elegant flowers.",
        "image": "🌼"
    }

}

# ----------------------------
# Home Page
# ----------------------------

@app.route("/")
def home():

    return render_template("index.html")


# ----------------------------
# Prediction Route
# ----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        features = [[

            float(data["sepal_length"]),
            float(data["sepal_width"]),
            float(data["petal_length"]),
            float(data["petal_width"])

        ]]

        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]

        confidence = round(max(probabilities) * 100, 2)

        flower = flowers[prediction]

        return jsonify({

            "prediction": flower["name"],

            "scientific": flower["scientific"],

            "description": flower["description"],

            "image": flower["image"],

            "confidence": confidence,

            "algorithm": "K-Nearest Neighbors (KNN)"

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 400


# ----------------------------
# Run Flask
# ----------------------------

if __name__ == "__main__":

    app.run(debug=True)