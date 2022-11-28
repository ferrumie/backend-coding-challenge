import json
import sys
import datetime
from planner_api.database import SessionLocal, engine
from planner_api import models

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("planning.json") as f:
    json_obj = json.loads(f.read())
    
    for obj in json_obj:
        try:
            # check if planner record does not exist
            qs = db.query(models.Planner).filter_by(original_id=obj['originalId'])
            if qs.count() == 0:
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
                    start_date=datetime.datetime.strptime(obj.get('startDate'), "%m/%d/%Y %I:%M %p") if obj.get('startDate') else "",
                    end_date=datetime.datetime.strptime(obj.get('endDate'), "%m/%d/%Y %I:%M %p") if obj.get('endDate') else "",
                    client_name=obj.get('clientName'),
                    client_id=obj['clientId'],
                    industry=obj.get('industry'),
                    required_skills=obj.get('requiredSkills'),
                    optional_skills=obj.get('optionalSkills'),
                    is_unassigned=obj.get('isUnassigned'),
                )
                db.add(planner_record)
                sys.stdout.write(f"planner of id {obj['originalId']} added\n")
            else:
                sys.stdout.write(f"planner of id {obj['originalId']} already exists in the database\n")
            sys.stdout.write("database succesfully populated\n")
        except ValueError as e:
            sys.stdout.write(f"required column missing {e}\n")
            continue 
    db.commit()

db.close()
