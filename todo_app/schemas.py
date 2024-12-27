from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoResponse(TodoCreate):
    id: int

    class Config:
        orm_mode = True

