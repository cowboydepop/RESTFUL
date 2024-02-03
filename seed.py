# seed.py

from app import app
from models import db, Cupcake

# Create an application context
with app.app_context():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # Create cupcake instances
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    # Add and commit instances
    db.session.add_all([c1, c2])
    db.session.commit()
