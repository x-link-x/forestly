from flask import Flask, render_template
from controllers.areas_controller import areas_blueprint
from controllers.varieties_controller import varieties_blueprint
from controllers.trees_controller import trees_blueprint

app = Flask(__name__)

app.register_blueprint(areas_blueprint)
app.register_blueprint(varieties_blueprint)
app.register_blueprint(trees_blueprint)

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