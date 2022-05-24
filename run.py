from flask import Flask, request, render_template, send_from_directory
from config import POSTS_DATA_PATH

from app.main.views import main_blueprint
from app.loader.views import loader_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run(debug=True)