from sqlalchemy import Column, Integer, String
from database import Base

# ---------------- User Table ----------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

# ---------------- Assessment Table ----------------

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    degree = Column(String)
    year = Column(String)
    total_score = Column(Integer)
    recommended_career = Column(String)