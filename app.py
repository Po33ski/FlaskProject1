from flask import Flask, request

app = Flask(__name__)

def calculator(op: str, arg1, arg2):
    if op == 'sum':
        return arg1 + arg2
    elif op == 'min':
        return arg1 - arg2
    elif op == 'mul':
        return arg1 * arg2
    elif op == 'div':
        return arg1 / arg2
    else: return None

def operator(op):
    if op == 'sum':
        return "+"
    elif op == 'min':
        return "-"
    elif op == 'mul':
        return "*"
    elif op == 'div':
        return "/"
    else: return None
@app.route('/calculate')
def calculate():  # put application's code here
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    result = calculator(op, arg1, arg2)

    return  str(arg1) + " " + operator(op) + " " +  str(arg2) + ' = ' + str(result)


if __name__ == '__main__':
    app.run()
