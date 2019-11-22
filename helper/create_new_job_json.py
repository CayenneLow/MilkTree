import json 
from models.Job import Job

# Creates a new JSON Object for a job to post to freelancer.
def create_new_job_json(job):

    job_dict = {
        "title": job.get_title(),
        "description": job.get_description(),
        "currency": {
            "id": job.get_currency(),
        },
        "budget": {
            "minimum": job.get_min_budget(),
            "maximum": job.get_max_budget(),
        },
        "jobs": job.get_skills() # skills 
        
    }

    json_dict = json.dumps(job_dict)
    return json_dict
