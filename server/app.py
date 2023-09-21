#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python operations with Flask Routing and Views</h1>'

@app.route('/print/<string:paramater>')
def print_string(parameter):
    print('Hello')
    # return f'{parameter}'

@app.route('/count/<int:num>')
def count(num):
    count=0
    for i  in range(num):
    # count += f'{i}/n'\
        count += num + 1

    return count 

@app.route('/math/<int:num1>/<string:operation<int:num2>')
def math(num1,num2,operation):
    if operation == '+':
        return str(num1+num2)
    
    elif operation == '-':
        return str(num1-num2)
    
    elif operation == '*':
        return str(num1*num2)
    
    elif operation == 'div':
        return str(num1/num2)
    
    elif operation == '%':
        return str(num1%num2)

    return 'Operators not found.Use the following operators +,'-',%'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
