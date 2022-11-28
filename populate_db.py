import json
import sys
from planner_api.database import SessionLocal, engine
from planner_api import models

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("planning.json", "r") as f:
    json_obj = json.loads(f)
    
    for obj in json_obj:
        try:
            # check if planner record does not exist
            qs = db.query(models.Planner).filter(original_id=obj['originalId'])
            if not qs.exists():
                planner_record = models.Planner(
                    original_id=obj['originalId'],
                    talent_id=obj.get('talentId'),
                    talent_grade=obj.get('talentGrade'),
                    talent_name=obj.get('talentName'),
                    booking_grade=obj.get('bookingGrade'),
                    operational_unit=obj['operatingUnit'],
                    office_city=obj.get('officeCity'),
                    office_postal_code=obj['officePostalCode'],
                    job_manager_name=obj.get('jobManagerName'),
                    job_manager_id=obj.get('jobManagerId'),
                    total_hours=obj['totalHours'],
                    start_date=obj.get(''),
                    end_date=obj.get(''),
                    client_name=obj.get('clientName'),
                    client_id=obj['clientId'],
                    industry=obj.get('industry'),
                    required_skills=obj.get('requiredSkills'),
                    optional_skills=obj.get('optionalSkills'),
                    is_unassigned=obj.get('isUnassigned'),
                )
                db.add(planner_record)
                sys.stdout.write(f"planner of id {obj['originalId']} added")
            else:
                sys.stdout.write(f"planner of id {obj['originalId']} already existed in the database")
            sys.stdout.write("database succesfully populated added")
        except ValueError:
            sys.stdout.write("required column missing")
            continue 

    db.commit()

db.close()