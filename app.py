import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fixed procedure for deterministic coefficients
seed = "FA23-BDS-044" 
random.seed(seed)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Accept input parameters through API call[cite: 2]
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
        x3 = float(request.args.get('x3', 0))
        
        # Linear regression equation[cite: 2, 3]
        y = (a1 * x1) + (a2 * x2) + (a3 * x3) + b
        
        # Return prediction as JSON response[cite: 2, 3]
        return jsonify({
            "registration number": seed,
            "prediction": round(y, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
