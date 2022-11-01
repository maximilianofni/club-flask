from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'flask es una mierda'

if __name__ == '__main__':
    app.run()
