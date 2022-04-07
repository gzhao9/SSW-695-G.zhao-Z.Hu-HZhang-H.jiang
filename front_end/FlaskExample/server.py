from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/login')
def hello():
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    json_str = json.dumps(data)
    return json_str


@app.route('/add', methods=['GET', 'POST'])
def add():
    res = {'sum': 0}
    data = json.loads(request.get_data())
    print(data)
    res['sum'] = data['one'] + data['two']
    json_str = json.dumps(res)
    return json_str


@app.route('/readUserDate')
def read_date():
    filename = 'USER_INFO_EXAMPLE.json'
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
