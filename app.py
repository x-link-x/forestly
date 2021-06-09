from flask import Flask, render_template
# import blueprints

app = Flask(__name__)

# register blueprints

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/forest")
def forest():
    return render_template("forest.html")


if __name__ == '__main__':
    app.run()