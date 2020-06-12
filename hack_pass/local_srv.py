import json
from flask import Flask, request, Response

app = Flask(__name__)

stats = {
    'attempts': 0,
    'success': 0
}


@app.route('/')
def hello():
    return f'Hello, user! stats={stats}'


@app.route('/auth', methods=['POST'])
def auth():
    stats['attempts'] += 1

    data = request.json
    login = data['login']
    password = data['password']

    with open('users.json') as f:
        users = json.load(f)

    if login in users and password == users[login]:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)


if __name__ == '__main__':
    app.run()
