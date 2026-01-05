from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)


class Preference(Base):
    __tablename__ = "preferences"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    preferred_colors = Column(String, nullable=False)  # stored as comma-separated
    preferred_style = Column(String, nullable=False)


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(String, nullable=False)
    action = Column(String, nullable=False)
