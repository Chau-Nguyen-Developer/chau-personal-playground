import re
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "Hello, Flask."

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. 
    # URL arguments can contain arbitrary text, so we restrict to safe characters only.
    # The code filters the name argumen to contain only letters, 
    # which avoids inject of control characters, HTML, and so forth.  
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    
    content = "Hello there, " + clean_name + "! It is " + formatted_now
    return content