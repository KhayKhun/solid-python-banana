from flask import Flask

app = Flask(__name__)

@app.route('/calculate/<int:a>/<int:b>')
def calculate(a, b):
    result = a*a + b*b
    return f"The sum of {a}^2 + {b}^2 is {result}"

if __name__ == '__main__':
    app.run(debug=True)