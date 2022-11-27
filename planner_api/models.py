from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, JSON, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from planner_api.database import Base


class Planner(Base):
    __tablename__ = "planner"
    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(String(255), nullable=False, index=True)
    talent_id = Column(String(255), index=True)
    talent_grade = Column(String(255))
    talent_name = Column(String(255), index=True)
    booking_grade = Column(String(255))
    operational_unit = Column(String(255), nullable=False)
    office_city = Column(String(255))
    office_postal_code = Column(String(255), nullable=False)
    job_manager_name = Column(String(255), index=True)
    job_manager_id = Column(String(255))
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    client_name = Column(String(255), index=True)
    client_id = Column(String(255), nullable=False)
    industry = Column(String(255))
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean)

    def __repr__(self):
        return "<Planner(talent_name='%s', talent_id='%s')>" % (
            self.talent_name,
            self.talent_id,
       )