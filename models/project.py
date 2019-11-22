from models.Job import Job 

class Project:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.location = None
        self.jobs = []

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_desc(self):
        return self.desc
    
    def set_desc(self, desc):
        self.desc = desc 
    
    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location 
    
    def get_jobs(self):
        return self.jobs 
    
    def add_job(self, job):
        self.jobs.append(job)
    
    def delete_job(self, job):
        self.jobs.remove(job)
    