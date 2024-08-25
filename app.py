from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def index():
    lista_personas = [
        {'name': 'Miguel Lopez Ariza'},
        {'name': 'Leonardo Lopez'},
        {'name': 'Carlos'},
        {'name': 'Jose'}
    ]
    return jsonify(lista_personas)

if __name__ == '__main__':
    app.run(debug=True)
