#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to the console
    return parameter  # Display in the browser

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'  # Add a newline at the end
    return numbers  # Return the plain newline-separated string


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):  # Fixing the syntax
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Handle invalid operations

    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(port=5555, debug=True)
