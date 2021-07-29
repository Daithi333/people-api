from app import db, ma


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Person({self.__dict__})'


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'balance', 'email', 'address')
