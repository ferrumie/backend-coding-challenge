from fastapi.testclient import TestClient
from planner_api.main import app, get_db
from planner_api import schemas
from fastapi_pagination import Page, add_pagination, paginate
from fastapi import Depends, FastAPI, Request, Response
import json
from tests.conftest import override_get_db
from planner_api import models
from tests.conftest import TestingSessionLocal, engine

client = TestClient(app)
add_pagination(app)

app.dependency_overrides[get_db] = override_get_db
models.Base.metadata.create_all(bind=engine)


def test_list_planners():
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

    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'items': [], 'page': 1, 'size': 50, 'total': 0}
    db.close()


def test_list_planners_with_filter():
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

    response = client.get('/ping?filter=total_hours,33.0-client_id,cl_1')
    assert response.status_code == 200
    assert response.json() == {'items': [], 'page': 1, 'size': 50, 'total': 0}
    db.close()


def test_list_planners_with_sort():
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

    response = client.get('/ping?sort=total_hours')
    assert response.status_code == 200
    assert response.json() == {'items': [], 'page': 1, 'size': 50, 'total': 0}
    db.close()
