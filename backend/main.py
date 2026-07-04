from fastapi import FastAPI
from database import engine, Base, SessionLocal
import models
import schemas
from questions import questions
from career_rules import recommend_career

# Create database tables
Base.metadata.create_all(bind=engine)

# Create database session
db = SessionLocal()

# Create FastAPI app
app = FastAPI()

# ---------------- Home API ----------------

@app.get("/")
def home():
    return {"message": "Welcome to AI Career Guidance System"}


# ---------------- Register API ----------------

@app.post("/register")
def register(user: schemas.UserCreate):
    return {
        "message": "Registration Successful",
        "user": user
    }


# ---------------- Login API ----------------

@app.post("/login")
def login(user: schemas.UserLogin):

    if (
        user.email == "wearstarfamilychimmiri@gmail.com"
        and user.password == "iloveyou20jk"
    ):
        return {
            "message": "Login Successful"
        }

    return {
        "message": "Invalid Email or Password"
    }


# ---------------- Questions API ----------------

@app.get("/questions")
def get_questions():
    return questions


# ---------------- Career Recommendation API ----------------

@app.post("/recommend")
def recommend(data: dict):

    answers = data["answers"]

    total_score = sum(answers)

    career = recommend_career(total_score)

    return {
        "total_score": total_score,
        "recommended_career": career
    }


# ---------------- Save Assessment API ----------------

@app.post("/save-assessment")
def save_assessment(data: schemas.AssessmentCreate):

    assessment = models.Assessment(
        name=data.name,
        age=data.age,
        degree=data.degree,
        year=data.year,
        total_score=data.total_score,
        recommended_career=data.recommended_career
    )

    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return {
        "message": "Assessment Saved Successfully"
    }