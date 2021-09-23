from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    name = 'sir'
    letters = list(name)
    #hi there
    mylist = [1,2,3,4,5]
    puppies = ['rufus','sammy','jake']
    return render_template('basic.html',name=name,letters=letters,mylist=mylist,puppies=puppies)

if __name__ == '__main__':
    app.run(debug=True)