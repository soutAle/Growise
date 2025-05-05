from backend.extensions import db

users_sector = db.Table('users_sector',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('sector_id', db.Integer, db.ForeignKey('sector.sector_id'), primary_key=True)
)

def __repr__(self):
    return f'<UserSector {self.user_id}, {self.sector_id}>'

def serialize(self):
    return {
        "user_id": self.user_id,
        "sector_id": self.sector_id
    }

