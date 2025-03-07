from flask import Flask, request, jsonify
from fpdf import FPDF

app = Flask(__name__)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Medication Report", ln=True, align='C')
    
    for med in data["medications"]:
        pdf.cell(200, 10, txt=f"Medicine: {med['name']}, Dosage: {med['dosage']}", ln=True)

    pdf.output("medication_report.pdf")
    return jsonify({"message": "PDF generated successfully", "file": "medication_report.pdf"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)