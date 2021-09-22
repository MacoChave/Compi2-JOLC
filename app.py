from ts import TablaSimbolo
from flask import Flask, render_template, request
from analizar import ejecutar_instrucciones
from gramatica import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/editor', methods=['GET'])
def editor():
    return render_template('editor.html')

@app.route('/analize', methods=['POST'])
def analize():
    if request.method == 'POST' :
        source = request.form['code']
        instrucciones = parse(source)
        tabla_simbolo = TablaSimbolo()
        global lista_errores
        result = ejecutar_instrucciones(instrucciones, tabla_simbolo, lista_errores)
    return render_template('editor.html', source = source, result = result)

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)