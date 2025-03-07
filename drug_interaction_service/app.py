from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample interaction data (in real implementation, query an external API or database)
drug_interactions = {
    ("Aspirin", "Warfarin"): "Increases bleeding risk",
    ("Ibuprofen", "Lisinopril"): "May reduce effectiveness of Lisinopril",
}

@app.route('/check_interaction', methods=['POST'])
def check_interaction():
    data = request.json
    meds = data["medications"]
    
    interactions_found = []
    for i in range(len(meds)):
        for j in range(i + 1, len(meds)):
            key = (meds[i], meds[j])
            reverse_key = (meds[j], meds[i])
            if key in drug_interactions:
                interactions_found.append({"drugs": key, "effect": drug_interactions[key]})
            elif reverse_key in drug_interactions:
                interactions_found.append({"drugs": reverse_key, "effect": drug_interactions[reverse_key]})

    return jsonify({"interactions": interactions_found})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)