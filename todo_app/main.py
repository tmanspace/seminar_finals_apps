from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base
from schemas import TodoCreate, TodoResponse
from db_funcs import create_todo, get_todos, get_todo_by_id, update_todo, delete_todo

app = FastAPI(title="TODO Service", version="1.0.0")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items", response_model=TodoResponse)
def create_item(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

@app.get("/items", response_model=list[TodoResponse])
def read_items(db: Session = Depends(get_db)):
    return get_todos(db)

@app.get("/items/{item_id}", response_model=TodoResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(db, item_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return todo

@app.put("/items/{item_id}", response_model=TodoResponse)
def update_item(item_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db, item_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_todo

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted_todo = delete_todo(db, item_id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
