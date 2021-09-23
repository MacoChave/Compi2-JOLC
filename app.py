from ts import TablaSimbolo
from flask import Flask, render_template, request
from analizar import *
from gramatica import *

app = Flask(__name__)

res = 0

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
    global response
    global res
    response = ''
    globales = TablaSimbolo()
    errores = []
    if request.method == 'POST' :
        source = request.form['code']
        instrucciones = parse(source)
        tabla_simbolo = TablaSimbolo()
        globales_inner = TablaSimbolo()
        res = ejecutar_instrucciones(instrucciones, tabla_simbolo, globales_inner)
    return render_template('editor.html', source = source, result = res[0], error = res[1])

@app.route('/reports')
def reports():
    global res
    return render_template('reports.html', error = res[1])

if __name__ == '__main__':
    app.run(debug=True)