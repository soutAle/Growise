from backend.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_role = db.Column(db.String(20), nullable=False, default='student')
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    experience = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    academic_level = db.Column(db.String(120), nullable=True)
    is_active = db.Column(db.Boolean(), default=True)
    is_available = db.Column(db.Boolean(), default=True)
    register_type = db.Column(db.String(20), nullable=False, default='local')

    knowledge_area_id = db.Column(db.Integer, db.ForeignKey('knowledge_area.knowledge_area_id'), nullable=True)
    knowledge_area = db.relationship('KnowledgeArea', back_populates='users', lazy=True)

    sector_id = db.Column(db.Integer, db.ForeignKey('sector.sector_id'), nullable=True)
    sector = db.relationship('Sector', back_populates='users', lazy=True)  # <--- Corregido

    sessions_attended = db.relationship(
        'SessionActive',
        foreign_keys='SessionActive.student_id',
        backref='student',
        lazy=True
    )

    sessions_created = db.relationship(
        'SessionActive',
        foreign_keys='SessionActive.teacher_id',
        backref='teacher',
        lazy=True
    )

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "description": self.description,
            "experience": self.experience,
            "phone": self.phone,
            "academic_level": self.academic_level,
            "sector": self.sector.serialize() if self.sector else None,
            "knowledge_area": self.knowledge_area.serialize() if self.knowledge_area else None,
            "sessions_attended": [s.serialize() for s in self.sessions_attended],
            "sessions_created": [s.serialize() for s in self.sessions_created],
            "is_active": self.is_active,
            "is_available": self.is_available,
            "current_role": self.current_role,
            "register_type": self.register_type
        }
