from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) 
@app.route('/')
def hello():
    return "Hi , Sorry u have to try http://127.0.0.1:5000/users  to display the HTML Table of all users"

@app.route('/users')
def user_info():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
    {'first_name' : 'Michael ', 'last_name' : 'Choi'},
    {'first_name' : 'John ', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark ', 'last_name' : 'Guillen'},
    {'first_name' : 'KB ', 'last_name' : 'Tonel'}
]          
    return render_template('lists.html',list_users = users)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 