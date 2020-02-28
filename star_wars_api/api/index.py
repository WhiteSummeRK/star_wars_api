from flask import current_app, Blueprint, render_template, jsonify

app = Blueprint('index', __name__)


@app.route('/')
def ship_index():
    return render_template(
        "index.html"
    )