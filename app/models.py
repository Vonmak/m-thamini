from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime(250), default=datetime.utcnow)
    asset = db.relationship('Asset', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    assetname = db.Column(db.String(255))
    category_id = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(), index=True)
    location = db.Column(db.String(255), nullable=False)
    worth = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_posted = db.Column(db.DateTime(250), default=datetime.utcnow)

    def save_assets(self):
        db.session.add(self)
        db.session.commit()

    def delete_asset(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_assets(cls):
        assets = Asset.query.filter_by(assets_id=id).all()
        return assets

    def __repr__(self):
        return f"Asset {self.assetname}"


class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'
