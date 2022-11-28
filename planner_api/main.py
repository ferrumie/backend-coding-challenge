from fastapi import FastAPI, Depends, Query
from planner_api import models, schemas
from fastapi_pagination import Page, paginate, add_pagination
from planner_api.database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text, or_
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

add_pagination(app)

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


@app.get("/ping")
def pong(db: Session = Depends(get_db)):
    qs = db.query(models.Planner)
    breakpoint()
    return paginate(qs.all())


@app.get("/planners", name="List all planners", response_model=Page[schemas.Planner])
def list_planners(
    db: Session = Depends(get_db),
    sort: str = Query(None, alias='sort'),
    filter: str = Query(None, alias='filter'),
) -> Page:
    """Get list of all planners"""
    if sort is not None:
        qs = db.query(models.Planner).order_by(text(sort))
    elif filter is not None:
        # receive in format filter=query_key,value-query_key,value
        # turn to {query_key: value, query_key:value}
        pair = dict(x.split(",") for x in filter.split("-"))
        pair_list = []
        for key, value in pair.items():
            _key = getattr(models.Planner, key)
            search = "%{}%".format(value)
            pair_list.append(_key.like(search))

        qs = db.query(models.Planner).filter(or_(*pair_list))
    else:
        qs = db.query(models.Planner)
    return paginate(qs.all())
