from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'write /plat in bar to start'  # Return the string 'Hello World!' as a response

@app.route('/play')
def repeat():
    return render_template('index.html')

@app.route('/play/<num>')
def num(num):
    return render_template('index2.html',_num = int(num))

@app.route('/play/<num>/<color>')
def color(num,color):
    return render_template('index3.html',_num = int(num) , _color=color)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 

