from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b
#
def sub(a, b):
    return a - b

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    if operation == 'add':
        result = add(a, b)
    elif operation == 'sub':
        result = sub(a, b)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)