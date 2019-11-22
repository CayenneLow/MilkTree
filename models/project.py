class Project:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.location = None
        self.jobs = []

    def get_title():
        return self.title
    
    def set_title(title):
        self.title = title
    
    def get_desc():
        return self.desc
    
    def set_desc(desc):
        self.desc = desc 
    
    def get_location():
        return self.location

    def set_location(location):
        self.location = location 
    
    def get_jobs():
        return self.jobs 
    
    def add_job(Job job):
        self.jobs.append(job)
    
    def delete_job(Job job):
        self.jobs.remove(job)
    