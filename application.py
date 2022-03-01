from flask import Flask
application = Flask(__name__)
app = application


@application.route('/')
def hello_world():
    return 'You better work!!.'

if __name__ == '__main__':
    app.run(debug=True)