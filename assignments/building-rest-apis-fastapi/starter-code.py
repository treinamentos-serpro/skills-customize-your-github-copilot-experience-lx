from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="School Tasks API")


class Task(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read the FastAPI guide", "description": None, "completed": False},
    {"id": 2, "title": "Build the first endpoint", "description": None, "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "School Tasks API is running"}


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    # TODO: Assign an id, store the task, and return the new task.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Find a task by id or raise an HTTPException with status 404.
    pass


@app.put("/tasks/{task_id}")
def replace_task(task_id: int, task: Task):
    # TODO: Replace an existing task or return status 404 when it is missing.
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: Remove an existing task or return status 404 when it is missing.
    pass