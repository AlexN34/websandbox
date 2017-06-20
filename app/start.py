import flask  #making code needed to build web apps available
# flask is framework, Flask is prototype used to create instances
app = flask.Flask(__name__) #creates instance of Flask class
#__name__ is special; gets as value of __main__ when script is executed

@app.route("/") #decorate hello() with "/" url - app.route gives url?
#when localhost:5000 accessed, home runs and returns its output on the page
#gives home url. /about/ requires localhost:5000/about/
def home():
    return flask.render_template('home.html')
@app.route("/about/")
def about():
    return flask.render_template('about.html')

#on execution of a script (helloFlask.py), python assigns
# __main__ as name (__name__ variable)
# we know this will happen when script runs so use it as condition to run app
if __name__ == "__main__":
    app.run(debug=True) #app is new Flask instance defined above
