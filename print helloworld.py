from flask import Flask #importing flask module and creating a Flask web server from the flask module
app =Flask(__name__) #creating an instance of Flask class.means creating a new web application (name=app) 

@app.route('/') #route is a decorative function. used to indicate default page like homepage
def hello():  #hello is the function
    return 'Hello World' #print Hello World.display on web page

if __name__ =='__main__': #checks if the script is being run directly 
    app.run(debug=True)   #function call starts the Flask web application in debug mode and The debug=True parameter enables debugging mode which allows developers to get detailed information about any errors that occur during the execution of the web application.
    

