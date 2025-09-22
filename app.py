import re
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/old_home")
def old_home():
    return "Hello, Flask."

@app.route("/")
@app.route("/new_home")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about/")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
@app.route("/contact/")
def contact():
    return render_template("contact.html")




# NEW HELLO_THERE FUNCTION
# Modify the hello_there function to use render_template() function inside 
# to load a template and apply the named values (and add a route to recognize the case without a name).
# Function render_template() assumes that the first argument is relative to the "templates" folder. 
# We can see that the below code is much simpler now. It only concerned with data values, 
# becuase the markup and formatting is all contained in template.
@app.route("/hello/<name>")
@app.route("/hello/")
def hello_there(name = None):
    return render_template(
        "hello_there.html", 
        name = name, 
        date = datetime.now()
    )

# Add a function with the route /api/data that returns the static data
# file using the send_static_file() method. 
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


#--------------------------------------------------------
#OLD HELLO_THERE FUNCTION
# def hello_there(name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Modify the format. The Flask server will auto reload, 
#     # which means the changes will be applied without the need to restart the debugger. 

#     # formatted_now = now.strftime("%D %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. 
#     # URL arguments can contain arbitrary text, so we restrict to safe characters only.
#     # The code filters the name argumen to contain only letters, 
#     # which avoids inject of control characters, HTML, and so forth.  
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

    
#     content = "Hello there, " + clean_name + "! It is " + formatted_now
#     return content