from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base
from schemas import URLCreate, URLResponse, URLStats
from db_funcs import create_short_url, get_short_url, get_url_stats

app = FastAPI(title="Short URL Service", version="1.0.0")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLResponse)
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    return create_short_url(db, data)

@app.get("/{short_id}")
def redirect_to_url(short_id: str, db: Session = Depends(get_db)):
    url = get_short_url(db, short_id)
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url.full_url)

@app.get("/stats/{short_id}", response_model=URLStats)
def get_url_statistics(short_id: str, db: Session = Depends(get_db)):
    stats = get_url_stats(db, short_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return stats
