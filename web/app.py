"""
John Doe's Flask API.
"""
from flask import Flask, render_template, send_from_directory, abort
import config # Configure from .ini files and command line
import os

app = Flask(__name__)

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html")

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")

@app.route("/<path:file>")
def respond(file):
    docroot = options.DOCROOT
    #filepath = os.path.join(docroot, file)
    if ('~' in file) or ('//' in file) or ('..' in file):
        return abort(403)
    elif file.endswith('.html' or '.css'):
        return send_from_directory(docroot, file)
    else:
        return abort(404)

if __name__ == "__main__":
    options = config.configuration()
    app.run(debug=True, host='0.0.0.0')
