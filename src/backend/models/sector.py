from backend.extensions import db
from backend.models.users_sector import users_sector

class Sector(db.Model):
    __tablename__ = 'sector'
    sector_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    num_sessions_active = db.Column(db.Integer, nullable=True, default=0)
    num_sessions_total = db.Column(db.Integer, nullable=True, default=0)
    knowledge_area_id = db.Column(db.Integer, db.ForeignKey('knowledge_area.knowledge_area_id'), nullable=False)

    sessions = db.relationship('SessionActive', back_populates='sector', lazy=True)
    users = db.relationship('User', secondary=users_sector, back_populates='sectors', lazy=True)
    knowledge_area = db.relationship('KnowledgeArea', back_populates='sectors', lazy=True)

    def __repr__(self):
        return f'<Sector {self.name}>'

    def serialize(self):
        return {
            "sector_id": self.sector_id,
            "name": self.name,
            "description": self.description,
            "knowledge_area_id": self.knowledge_area_id,
            "num_sessions_active": self.num_sessions_active,
            "num_sessions_total": self.num_sessions_total,
            "sessions": [session.serialize() for session in self.sessions],
            "users": [user.serialize() for user in self.users]
        }
