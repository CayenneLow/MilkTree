class Job:
    def __init__(self, job_id = -1, title = "", description = "", \
                    budget = 0, currency = "", location = None, \
                    skills = [], userId = 0):
        self.job_id = -1
        self.title = ""
        self.description = ""
        self.budget = 0
        self.currency = ""
        self.location = None
        self.skills = []
        self.userId = 0 #freelancer user id

    def set_job_id(self, id):
        self.id = id
    
    def get_job_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_budget(self, budget):
        self.budget = budget

    def set_currency(self, currency):
        self.currency = currency

    def set_location(self, location):
        self.location = location

    def set_userId(self, userId):
        self.userId = userId

    def add_skill(self, skill):
        self.skills.append(skill)

    def remove_skill(self, skill):
        self.skills.remove(skill)

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_budget(self):
        return self.budget

    def get_currency(self):
        return self.currency

    def get_location(self):
        return self.location

    def get_userId(self):
        return self.userId

    def get_skills(self):
        return self.skills
