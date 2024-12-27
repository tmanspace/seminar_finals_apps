from sqlalchemy.orm import Session

from models import Todo
from schemas import TodoCreate

def create_todo(db: Session, todo_data: TodoCreate) -> Todo:
    todo = Todo(**todo_data.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_todos(db: Session):
    return db.query(Todo).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo_id: int, todo_data: TodoCreate):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    for key, value in todo_data.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return todo
