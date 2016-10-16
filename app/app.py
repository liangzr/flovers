# coding:utf-8
from flask import Flask, url_for
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('app', 'templates/jinja2'))


@app.route('/')
def index():
    return env.get_template('index.html').render(
        title='Hello',
        content='this is my first app')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
