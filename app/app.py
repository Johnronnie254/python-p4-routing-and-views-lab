from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:operation>')
def print_string(operation):
    return f'<h1>Print {operation}</h1>'
@app.route('/count/<int:number>')
def count(number):
    numbers_str = '\n'.join(str(x) for x in range(1, number + 1))
    return f'<h1>Count:<br>{numbers_str}</h1>'
@app.route('/<string:operation>/<float:num1>/<float:num2>')
def math(operation, num1, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h1>Error: Division by zero</h1>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Error: Invalid operation</h1>'

    return f'<h1>Result: {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
