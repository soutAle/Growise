from backend.extensions import db

class KnowledgeArea(db.Model):
    knowledge_area_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    num_sessions_active = db.Column(db.Integer, default=0)
    num_sessions_total = db.Column(db.Integer, default=0)
    num_sessions_completed = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)

    sectors = db.relationship('Sector', back_populates='knowledge_area', lazy=True)
    sessions = db.relationship('SessionActive', back_populates='knowledge_area', lazy=True)
    users = db.relationship('User', back_populates='knowledge_area', lazy=True)

    def __repr__(self):
        return f'<KnowledgeArea {self.name}>'

    def serialize(self):
        return {
            "knowledge_area_id": self.knowledge_area_id,
            "name": self.name,
            "description": self.description,
            "num_sessions_active": self.num_sessions_active,
            "num_sessions_total": self.num_sessions_total,
            "num_sessions_completed": self.num_sessions_completed,
            "sectors": [sector.serialize() for sector in self.sectors]
        }