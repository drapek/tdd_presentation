import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/random_user')
def random_user():
    users = ['Krzysztof Krawczyk', 'Otylia Jędrzejczak', 'Janosik']
    return random.choice(users)


if __name__ == '__main__':
    app.run()
