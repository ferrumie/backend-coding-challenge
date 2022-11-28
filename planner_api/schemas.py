from datetime import datetime
from typing import Union

from pydantic import BaseModel


class Planner(BaseModel):
    id: int
    original_id: str
    talent_id: str
    talent_grade: str
    talent_name: str
    booking_grade: str
    operational_unit: str
    office_city: str
    office_postal_code: str
    job_manager_name: str
    job_manager_id: str
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_name: str
    client_id: str
    industry: str
    required_skills: dict
    optional_skills: dict
    is_unassigned: bool

    class Config:
        orm_mode = True
