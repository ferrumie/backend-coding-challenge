import json

from fastapi import Depends, FastAPI, Request, Response
from fastapi.testclient import TestClient
from fastapi_pagination import Page, add_pagination, paginate

from planner_api import models, schemas
from planner_api.main import app, get_db
from tests.conftest import TestingSessionLocal, engine, override_get_db

client = TestClient(app)


app.dependency_overrides[get_db] = override_get_db
models.Base.metadata.create_all(bind=engine)


def load_data() -> None:
    # create model
    with open("./planning.json") as f:
        json_obj = json.loads(f.read())
        db = TestingSessionLocal()

    for obj in json_obj[:10]:
        planner_record = models.Planner(
            original_id=obj['originalId'],
            operational_unit=obj['operatingUnit'],
            office_postal_code=obj['officePostalCode'],
            total_hours=obj['totalHours'],
            client_id=obj['clientId'],
        )
        db.add(planner_record)
    db.commit()
    db.close()


def test_list_planners(test_db):
    add_pagination(app)
    load_data()
    response = client.get('/planners')
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.json().get('size') == 50
    assert response.json().get('total') == 10


def test_list_planners_with_filter(test_db):
    load_data()
    response = client.get('/planners?filter=total_hours,33.0-client_id,cl_1')
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.json().get('size') == 50
    assert response.json().get('total') == 10


def test_list_planners_with_sort(test_db):
    load_data()
    response = client.get('/planners?sort=total_hours')
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.json().get('size') == 50
    assert response.json().get('total') == 10


def test_list_planners_with_custom_size(test_db):
    load_data()
    response = client.get('/planners?size=10')
    assert response.status_code == 200
    assert response.json().get('size') == 10
    assert response.json().get('total') == 10
