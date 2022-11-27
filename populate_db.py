import json
from planner_api.database import SessionLocal, engine
from planner_api import models

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

