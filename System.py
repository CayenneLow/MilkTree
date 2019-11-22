from models.project import Project

class System:
    def __init__(self):
        self.users = []
        self.projects = []

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def get_projects(self):
        return self.projects

    def set_projects(self, projects):
        self.projects = projects

    def add_user(self, user):
        self.users.append(user)

    def add_project(self, project):
        self.projects.append(project)

    def find_project(self, project_id):
        for project in self.projects:
            if project.get_proj_id() == project_id:
                return project
        return None

    def remove_project(self, project_id):
        for project in self.projects:
            if project.get_proj_id() == project_id:
                self.projects.remove(project)
                return

    def get_n_projects(self):
        return len(self.projects)
