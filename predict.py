import pickle
from flask import Flask, request, jsonify

model_file = 'model.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f:
    model = pickle.load(f)

with open(dv_file, 'rb') as f:
    dv = pickle.load(f)

app = Flask('admission')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    client = request.get_json()
    X = dv.transform([client])

    y_pred = model.predict_proba(X)[0, 1]
    admit = y_pred >= 0.5

    result = {
        "admission_probability": y_pred,
        "admission": bool(admit)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
