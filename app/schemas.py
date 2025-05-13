from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    

class Task(TaskCreate):
    id: int

    class Config:
        from_attributes = True    
        