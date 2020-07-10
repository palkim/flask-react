import flask

app = flask.Flask("__main__")


@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello World, I am Flask, serving React")


app.run(debug=True)
