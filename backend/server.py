from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

@app.route('/calculate', methods=['POST'])  # Ensure 'POST' is included here
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if operation == 'plus':
        result = num1 + num2
    elif operation == 'minus':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    else:
        result = 'Invalid operation'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
