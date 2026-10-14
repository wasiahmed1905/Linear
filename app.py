from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# --- STUDENT REGISTRATION & SEED CONFIGURATION ---
REGISTRATION_NUMBER = "FA23-BDS-044"  # Replace with your registration number

# Convert student roll number to a deterministic integer seed
# Extract digits or hash string if roll number contains letters
SEED = int(''.join(filter(str.isdigit, REGISTRATION_NUMBER)))

# Generate fixed coefficients using the required procedure
random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Extract query parameters x1, x2, x3 from request URL
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
        x3 = float(request.args.get('x3', 0))

        # Calculate prediction using linear regression formula
        # y = a1*x1 + a2*x2 + a3*x3 + b
        prediction_val = (a1 * x1) + (a2 * x2) + (a3 * x3) + b

        # Format JSON response
        response = {
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction_val, 2)
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Listen on all network interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
