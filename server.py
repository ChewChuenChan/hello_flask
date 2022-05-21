from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# localhost:5000/say/<name> - have it say "Hi <NAME>!
# Bonus: Ensure the name provided are strings
@app.route('/say/<string:name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    x = name.capitalize()
    return f"Hi {x}!"

# localhost:5000/repeat/<int:num>/<string:name> - have it repeat <string:name> <int:num> times!
# Bonus: Ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    output = ''
    for i in range(0,num):
        output += f"<p>{name}</p> "
    return output

# Bonus: Ensure if the user types in any route other the previous
# they will receive an error message
@app.route('/<string:other>')
def error(other):
    return f"Sorry! No response. Try again."


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


