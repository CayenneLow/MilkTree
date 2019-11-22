from models.project import Project
from models.Job import Job

def init_packages():
    projectList = []
    newProject = Project("Marketing Starter Pack", "Specially tailored for startups looking to get the word out about their business", 1)
    newProject.add_job(Job(title="SEO - Search Engine Optimization", skills=["SEO"]))
    newProject.add_job(Job(title="Graphic Design", skills=["Graphic Design"]))
    newProject.add_job(Job(title="Digital Marketing", skills=["Digital Marketing"]))
    projectList.append(newProject) 
    newProject = Project("Startup Starter Pack", "Specially tailored for ambitious entrepreneurs looking to take the first step into startups", 2)
    newProject.add_job(Job(title="Tax Law", skills=["Tax Law"]))
    newProject.add_job(Job(title="Marketing", skills=["Marketing"]))
    newProject.add_job(Job(title="Customer Service", skills=["Customer Service"]))
    projectList.append(newProject) 
    newProject = Project("Filmmakers Starter Pack", "Specially tailored for aspiring filmmakers looking to make it big in the industry", 3)
    newProject.add_job(Job(title="Ghostwriting", skills=["Ghostwriting"]))
    newProject.add_job(Job(title="Photography", skills=["Photography"]))
    newProject.add_job(Job(title="Video Editing", skills=["Video Editing"]))
    projectList.append(newProject) 
    return projectList