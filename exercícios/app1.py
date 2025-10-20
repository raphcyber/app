from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('indexexercicio1.html')

@app.route('/sobre')
def sobre():
    return render_template('sobreexercicio1.html')

@app.route('/contatos')
def contatos():
    return render_template('contatosexercicio1.html')

if __name__ == '__main__':
    app.run(debug=True)
