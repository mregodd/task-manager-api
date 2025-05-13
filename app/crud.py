from sqlalchemy.orm import Session
from . import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task_id: int, updated_task: schemas.TaskCreate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        task.completed = updated_task.completed
        db.commit()
        db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task