from pydantic import BaseModel

# ---------------- User Schemas ----------------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


# ---------------- Assessment Schema ----------------

class AssessmentCreate(BaseModel):
    name: str
    age: int
    degree: str
    year: str
    total_score: int
    recommended_career: str