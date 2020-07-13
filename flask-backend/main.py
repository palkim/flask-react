import flask
from flask import render_template
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

app = flask.Flask("__main__")

# database server connection
# engine = create_engine('mssql+pyodbc://starraider:Marks&Spencer@starraider.database.windows.net/starraider.database'
#                       '.windows.net')
# conn = engine.connect()

# sql query
# result = conn.execute(“select Data from HelloWorld”)

# with engine.connect() as connection:
#    result = connection.execute("select Data from HelloWorld")


@app.route("/")
def my_index():
    # returns the index.html file from templates folder with token variable which includes the sql query result
    # return flask.render_template("index.html", token=result) 
    return flask.render_template("index.html", token="Hello Flask+React!")


app.run(debug=True)
