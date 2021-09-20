from flask import Flask #from flask package we are importing Flask class 
app = Flask(__name__) #created a application object

@app.route('/') #decorator which will take us to homepage
def index():
    return '<h1> Hello Puppy!</h1>' 

@app.route('/information') #for multiple pages in our website
def info():
    return '<h1> Puppies are cute! </h1>'

#dynamic route
@app.route('/puppy_latin/<name>')
def puppy(name):
    if name.endswith('y') == False:
        return '<h1> This is page for {} </h1>'.format(name + 'y')
    
    else:
        return '<h1> This is page for {} </h1>'.format(name[0:len(name)-1] + 'iful')

if __name__ == '__main__':
    app.run()  