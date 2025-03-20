from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

def calculate_bmi(height_cm, weight):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return round(bmi, 2), status

@app.route("/bmi", methods=["GET"])
def bmi_calculator():
    try:
        height_cm = float(request.args.get("height", 0))
        weight = float(request.args.get("weight", 0))

        if height_cm <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive numbers."}), 400

        bmi, status = calculate_bmi(height_cm, weight)
        return jsonify({"bmi": bmi, "status": status})
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter numeric values."}), 400

if __name__ == "__main__":
    app.run(debug=True)