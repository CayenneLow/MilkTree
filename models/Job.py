class Job:
    def __init__(self, job_id = -1, title = "", description = "", \
                    budget_min = 0, budget_max = 0, currency = "", location = None, \
                    skills = [], userId = 0, skill_names = [], job_link = ""):
        self.job_id = job_id
        self.title = title
        self.description = description
        self.budget_min = budget_min
        self.budget_max = budget_max
        self.currency = currency
        self.location = location
        self.skills = skills
        self.skill_names = skill_names
        self.userId = userId #freelancer user id
        self.job_link = job_link

    def set_job_link(self, job_link):
        self.job_link = job_link
    
    def get_job_link(self):
        return self.job_link
        
    def set_skill_names(self, skill_names):
        self.skill_names = skill_names
    
    def get_skill_names(self):
        return self.skill_names

    def set_job_id(self, id):
        self.id = id
    
    def get_job_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_currency(self, currency):
        self.currency = currency

    def set_location(self, location):
        self.location = location

    def set_userId(self, userId):
        self.userId = userId

    def set_budget_max(self, budget_max):
        self.budget_max = budget_max

    def set_budget_min(self, budget_min):
        self.budget_min = budget_min

    def add_skill(self, skill):
        self.skills.append(skill)

    def set_skills(self, skills):
        self.skills = skills

    def remove_skill(self, skill):
        self.skills.remove(skill)

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_currency(self):
        return self.currency

    def get_location(self):
        return self.location

    def get_userId(self):
        return self.userId

    def get_skills(self):
        return self.skills

    def get_budget_max(self):
        return self.budget_max

    def get_budget_min(self):
        return self.budget_min
