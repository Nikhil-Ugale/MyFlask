from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    name = 'sir'
    letters = list(name)
    #hi there
    return render_template('basic.html',name=name,letters=letters)

if __name__ == '__main__':
    app.run(debug=True)