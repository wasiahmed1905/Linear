import os
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

ROLL_NUMBER = os.environ.get("STUDENT_ROLL_NUMBER", "44")

# Seed must be an INT when the roll number is numeric —
# random.seed("44") != random.seed(44)!
seed = int(ROLL_NUMBER) if str(ROLL_NUMBER).isdigit() else ROLL_NUMBER
random.seed(seed)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b  = random.uniform(-10, 10)

print(f"[INIT] Seed={seed} -> a1={a1}, a2={a2}, a3={a3}, b={b}")

@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args.get("x1"))
        x2 = float(request.args.get("x2"))
        x3 = float(request.args.get("x3"))
    except (TypeError, ValueError):
        return jsonify({"error": "x1, x2, x3 are required numeric query params"}), 400

    prediction = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({
        "registration number": ROLL_NUMBER,
        "prediction": round(prediction, 2)
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "up"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
