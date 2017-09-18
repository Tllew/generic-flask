# generic-flask/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return 'Hey, we have Flask in a Docker container! %s'%name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')