from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/soma', methods=['GET'])
def somar():
    numero1 = float(request.args.get("valor1"))
    numero2 = float(request.args.get("valor2"))
    resultado = numero1 + numero2
    return jsonify({"resultado" : resultado}), 200

@app.route('/subtrair', methods=['GET'])
def subtrair():
    numero1 = float(request.args.get("valor1"))
    numero2 = float(request.args.get("valor2"))
    resultado = numero1 - numero2
    return jsonify({"resultado" : resultado}), 200

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    numero1 = float(request.args.get("valor1"))
    numero2 = float(request.args.get("valor2"))
    resultado = numero1 * numero2
    return jsonify({"resultado" : resultado}), 200


@app.route('/dividir', methods=['GET'])
def dividir():
    numero1 = float(request.args.get("valor1"))
    numero2 = float(request.args.get("valor2"))
    resultado = numero1 / numero2
    if resultado == 0:
        return {"erro": "Divisão por zero não permitida"}
    return jsonify({"resultado" : resultado}), 200

if __name__ == "__main__":
    app.run(debug=True)