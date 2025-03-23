from flask import Flask, request, jsonify
from tee_emulator import run_private_inference

app = Flask(__name__)

@app.route('/inference', methods=['POST'])
def inference():
    user_input = request.json.get("message")
    result = run_private_inference(user_input)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
