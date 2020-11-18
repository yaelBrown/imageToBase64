from flask import Flask, render_template
from flask_cors import CORS

from imageController import imageController

app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*"}})


app.register_blueprint(imageController)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)