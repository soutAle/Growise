from backend.extensions import db

class SessionActive(db.Model):
    __tablename__ = 'session_active'
    session_active_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)

    sector_id = db.Column(db.Integer, db.ForeignKey('sector.sector_id'), nullable=False)
    knowledge_area_id = db.Column(db.Integer, db.ForeignKey('knowledge_area.knowledge_area_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    # Relaciones
    sector = db.relationship('Sector', back_populates='sessions', lazy=True)
    knowledge_area = db.relationship('KnowledgeArea', back_populates='sessions', lazy=True)

    def __repr__(self):
        return f'<SessionActive {self.name}>'

    def serialize(self):
        return {
            "session_active_id": self.session_active_id,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "sector": self.sector.serialize() if self.sector else None,
            "knowledge_area": self.knowledge_area.serialize() if self.knowledge_area else None,
            "teacher": self.teacher.serialize() if self.teacher else None,
            "student": self.student.serialize() if self.student else None
        }
