from datetime import datetime
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')


class Planner(BaseModel):
    id: int
    original_id: str
    talent_id: Optional[str]
    talent_grade: Optional[str]
    talent_name: Optional[str]
    booking_grade: Optional[str]
    operational_unit: str
    office_city: Optional[str]
    office_postal_code: str
    job_manager_name: Optional[str]
    job_manager_id: Optional[str]
    total_hours: float
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    client_name: Optional[str]
    client_id: str
    industry: Optional[str]
    required_skills: Optional[dict]
    optional_skills: Optional[dict]
    is_unassigned: Optional[bool]

    class Config:
        orm_mode = True
