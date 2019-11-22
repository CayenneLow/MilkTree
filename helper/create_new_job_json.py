import json 
from models.Job import Job

# Creates a new JSON Object for a job to post to freelancer.
def create_new_job_json(job):
    job = {
        "title": job.get_title(),
        "description": job.get_description(),
        "currency": {
            "id": currency_id
        },
        "budget": {
            "minimum": budget_min,
            "maximum": budget_max
        },
        "jobs": []
    }

    return json.dumps(job)
