from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    nome = 'Rogério'
    linguagem = 'Python'
    return render_template('index.html', nome=nome, linguagem=linguagem)

if __name__ == '__main__':
    app.run(debug=True)
