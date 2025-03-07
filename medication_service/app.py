from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample medication database
medications = []

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    data = request.json
    medicine = {"id": len(medications) + 1, "name": data["name"], "dosage": data["dosage"]}
    medications.append(medicine)
    return jsonify({"message": "Medicine added", "medicine": medicine})

@app.route('/medications', methods=['GET'])
def get_medications():
    return jsonify(medications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)