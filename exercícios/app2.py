from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    nomes = ['Rogério', 'Rosane', 'Judite', 'Agnes']
    return render_template('nomes.html', nomes=nomes)

if __name__ == '__main__':
    app.run(debug=True)