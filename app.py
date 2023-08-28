from flask import Flask

# creates app obj with flask class, __name__ gives the file unq name
app = Flask(__name__)

# decorator indicates browser endpoint

# '/' for the homepage


@app.route('/')
def homepage():
    return '''this is the homepage
             <p><a href = "/hello"><button>go to hello</button></a></p>'''


# hello page
@app.route('/hello')
def hello():
    return 'Hello, Im Rayhan'


# hosting locally; why port 5000?
app.run(host='localhost', port=5000)
