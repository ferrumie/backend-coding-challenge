from fastapi import FastAPI, Depends
from planner_api import models, schemas
from planner_api.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/planners/", response_model=list[schemas.Planner])
def show_records(db: Session = Depends(get_db)):
    """Get list of all planners"""
    planners = db.query(models.Planner).all()
    return planners