from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/editor', methods=['GET'])
def editor():
    return render_template('editor.html')

@app.route('/analize', methods=['POST'])
def analize():
    return 'Analize page works!'

@app.route('/reports')
def reports():
    return 'Reports page works!'

if __name__ == '__main__':
    app.run()