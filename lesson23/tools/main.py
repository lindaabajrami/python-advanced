from fastapi import FastAPI
from matplotlib.testing.widgets import do_event
from numpy.random import sample
from tenacity import retry

from models import Developer,Project

app = FastAPI()

@app.post("/developers")
def create_developer(developer: Developer)
    return {"message": "Developer created", "developer": developer}

@app.post("/projects")
def create_project(project: Project):
    return {"message": "Project created", "project": project}

@app.get("/projects")
def get_projects():
    sample_project = Project(
    title="Test",
    description= "This is a test project",
    language = ["Python", "JavaScript"],
    lead_developer=Developer(name="John Doe", experience=5)
    )

    return {"project": [sample_project]}
