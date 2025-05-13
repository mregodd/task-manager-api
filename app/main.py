from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.get("/")
def read_root():
    return {"message": "Task Manager API aktif!"}


# Tüm taskları listeler
@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


# Task oluşturur
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

# ID'ye göre task sorgular
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Belirtilen task bulunamadı.")
    return task


# Hedeflenen taskı günceller
@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, updated_task)
    if task is None:
        raise HTTPException(status_code=404, detail="Güncellenecek task bulunamadı.")
    return task


# Taskı siler
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Silinecek task bulunamadı.")
    return {"message": "Task silindi."}