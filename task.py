from flask import Flask, request

app = Flask(__name__)


@app.route('/find-root')
def find_root():
    args = request.args
    if not set(['a', 'b', 'c']).issubset(set(args.keys())):
        return {'result': False, 'error': 'Not enough arguments. You must provide a, b, c arguments'}

    try:
        a = int(args['a'])
        b = int(args['b'])
        c = int(args['c'])
    except:
        return {'result': False, 'error': 'Arguments a, b, c must be integers'}

    if a == 0:
        return {'result': True, 'solutions': [-c/b]}

    D = b**2 - 4*a*c

    if D < 0:
        return {'result': True, 'solutions': []}

    elif D == 0:
        return {'result': True, 'solutions': [-b/(2*a)]}

    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)

    return {'result': True, 'solutions': [x1, x2]}


@app.route('/guess/<int:num>')
def guess(num: int):
    if num < 1 or num > 100:
        return {'result': False, 'error': 'Number must be in range [1, 100]'}
    return {'result': True, 'color': 'blue'}
