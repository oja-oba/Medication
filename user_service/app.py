from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user database (in-memory)
users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = {"id": len(users) + 1, "name": data["name"], "role": data["role"]}
    users.append(user)
    return jsonify({"message": "User registered", "user": user})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)