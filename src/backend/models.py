from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

#  E.G User model
# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     user_type = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50))
#     testimony = db.Column(db.String(250))
#     image = db.Column(db.String(250))
#     telephone = db.Column(db.String(30), unique=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(180), nullable=False)
#     is_active = db.Column(db.Boolean, default=False)
#     country = db.Column(db.String(20))

#     profile_developer = db.relationship("Developer", backref="user", uselist=False)
#     profile_company = db.relationship("Company", backref="user", uselist=False)
#     candidates = db.relationship("Candidate", backref="user", lazy=True)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             'user_type': self.user_type,
#             "last_name": self.last_name,
#             "testimony": self.testimony,
#             "image": self.image,
#             "telephone": self.telephone,
#             "email": self.email,
#             "is_active": self.is_active,
#             "country": self.country,
#             "profile_developer": self.profile_developer.serialize() if self.profile_developer else None,
#             "profile_company": self.profile_company.serialize() if self.profile_company else None,
#             "candidates": [candidate.serialize() for candidate in self.candidates] if self.candidates else None
#         }