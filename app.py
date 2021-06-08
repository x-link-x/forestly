from flask import Flask, render_template
# import blueprints

app = Flask(__name__)

# register blueprints

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()