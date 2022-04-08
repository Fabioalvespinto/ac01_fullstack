import os
from flask import Flask, render_template, request, jsonify
from math import sqrt


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('ac.html')


@app.route('/calculadora', methods=['POST', 'GET'])
def result():
    getRequest = request.form.get
    valor1 = getRequest('v1')
    valor2 = getRequest('v2')
    operacao = request.form['operacao']

    if valor1 and valor2:
        if operacao == '+':
            return jsonify(float(valor1) + float(valor2))
        elif operacao == '-':
            return jsonify(float(valor1) - float(valor2))
        elif operacao == '/':
            return jsonify(float(valor1) / float(valor2))
        elif operacao == '*':
            return jsonify(float(valor1) * float(valor2))
        else:
            return 'error'
    else:
        return 'error'
    

if __name__ == '__main__':
    app.run(host='localhost' , port=5002, debug=True)