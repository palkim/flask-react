import flask
from flask import render_template
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

app = flask.Flask("__main__")

# database server connection
# server = 'starraider.database.windows.net' 
# database = 'starraider.database.windows.net' 
# username = 'starraider' 
# password = 'Marks&Spencer' 
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = conn.cursor()

# sql query
# result = conn.execute(“select Data from HelloWorld”)


@app.route("/")
def my_index():
    # returns the index.html file from templates folder with token variable which includes the sql query result
    # return flask.render_template("index.html", token=result) 
    return flask.render_template("index.html", token="Hello Flask+React!")


app.run(debug=True)
