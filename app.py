from ts import TablaSimbolo
from flask import Flask, render_template, request
from analizar import *
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
    global globales
    global errores
    globales = TablaSimbolo()
    errores = []
    if request.method == 'POST' :
        source = request.form['code']
        instrucciones = parse(source)
        tabla_simbolo = TablaSimbolo()
        globales_inner = TablaSimbolo()
        res = ejecutar_instrucciones(instrucciones, tabla_simbolo, globales_inner)
    return render_template('editor.html', source = source, result = res)

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)