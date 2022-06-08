from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!' 

@app.route('/say/<name>')
def name(name):
    return "Hi " + name 

@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    return render_template('name.html',_num = int(num),_name = name)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 

