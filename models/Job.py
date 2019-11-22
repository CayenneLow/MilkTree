class Job:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.budget = 0
        self.currency = ""
        self.location = None
        self.skills = []
        self.userId = 0 #freelancer user id

    def set_title(title):
        self.title = title

    def set_description(description):
        self.description = description

    def set_budget(budget):
        self.budget = budget

    def set_currency(currency):
        self.currency = currency

    def set_location(location):
        self.location = location

    def set_userId(userId):
        self.userId = userId

    def add_skill(skill):
        self.skills.append(skill)

    def remove_skill(skill):
        self.skills.remove(skill)

    def get_title:
        return self.title

    def get_description:
        return self.description

    def get_budget:
        return self.budget

    def get_currency:
        return self.currency

    def get_location:
        return self.location

    def get_userId:
        return self.userId

    def get_skills:
        return self.skills
