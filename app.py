"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect to the database
db.init_app(app)
db.create_all()

# Debug Toolbar setup
toolbar = DebugToolbarExtension(app)

# ... rest of your app code ...




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route("/")
def root():
    """Render homepage."""
    return render_template("index.html")


@app.route("/api/cupcakes")
def list_cupcakes():
    """Return all cupcakes in the system."""
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake and return data about the new cupcake."""
    data = request.json
    image = data.get('image', None)
    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=image
    )
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict()), 201


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Return data on a specific cupcake."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from data in the request. Return updated data."""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    for key, value in data.items():
        setattr(cupcake, key, value)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake and return confirmation message."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
