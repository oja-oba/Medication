from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample appointment database
appointments = []

@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    data = request.json
    appointment = {"id": len(appointments) + 1, "date": data["date"], "recipient": data["recipient"]}
    appointments.append(appointment)
    return jsonify({"message": "Appointment scheduled", "appointment": appointment})

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)