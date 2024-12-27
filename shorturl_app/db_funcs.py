import string
import random

from sqlalchemy.orm import Session

from models import ShortURL
from schemas import URLCreate

def generate_short_id(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(db: Session, data: URLCreate):
    short_id = generate_short_id()
    while db.query(ShortURL).filter(ShortURL.short_id == short_id).first():
        short_id = generate_short_id()
    short_url = ShortURL(short_id=short_id, full_url=str(data.url), visits=0)
    db.add(short_url)
    db.commit()
    db.refresh(short_url)
    return short_url

def get_short_url(db: Session, short_id: str):
    return db.query(ShortURL).filter(ShortURL.short_id == short_id).first()

def get_url_stats(db: Session, short_id: str):
    return db.query(ShortURL).filter(ShortURL.short_id == short_id).first()
