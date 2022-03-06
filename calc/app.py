# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


#makes new server 
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

#route for addition 
@app.route('/add')
def add_vals():
    """add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  add(a,b)
    
    return str(result)


#route for subtraction
@app.route('/sub')
def sub_vals():
    """subtract a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  sub(a,b)
    
    return str(result)

#route for multiplication 
@app.route('/mult')
def mult_vals():
    """multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  mult(a,b)
    
    return str(result)

#route for division
@app.route('/div')
def divide_vals():
    """add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  div(a,b)
    
    return str(result)