from flask import Flask, render_template 
app = Flask(__name__)  
@app.route('/')          
def index():
    return render_template('index.html')
@app.route('/<num>')
def index2(num):
    return render_template('index2.html' ,_num=int(num))

@app.route('/<x>/<y>')
def index3(x , y):
    return render_template('index3.html', _num1=int(x) , _num2=int(y))

if __name__=="__main__":   
    app.run(debug=True) 

