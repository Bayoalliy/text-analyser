from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/strings', methods=['POST'], strict_slashes=False)
def create_string():
    val = request.form.get('value')
    if not val:
        return jsonify({"Bad request": 'Invalid request body or missing "value" field'}), 400
    if not isinstance(val, str):
        return jsonify({'Unprocessable Entity': 'Invalid data type for "value" (must be string)'}), 422

    


if __name__ == '__main__':
    app.run(debug=True)
