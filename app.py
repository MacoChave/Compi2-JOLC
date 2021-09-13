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
        ejecutar_instrucciones(instrucciones)
    return 'Analize works!'

@app.route('/reports')
def reports():
    return 'Reports page works!'

if __name__ == '__main__':
    app.run(debug=True)