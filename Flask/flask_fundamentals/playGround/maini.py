from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'write /play to start' 

@app.route('/play')
def repeat():
    return render_template('index.html')

@app.route('/play/<num>')
def num(num):
    return render_template('index2.html',_num = int(num))

@app.route('/play/<num>/<color>')
def color(num,color):
    return render_template('index3.html',_num = int(num) , _color=color)
if __name__=="__main__":  
    app.run(debug=True) 

