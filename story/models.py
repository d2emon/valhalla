from app import db


class Hero(db.Model):
    """
    Create a Hero table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Hero: {}>'.format(self.name)

    @property
    def image_url(self):
        return "images/heroes/%d.jpg" % (self.id)
