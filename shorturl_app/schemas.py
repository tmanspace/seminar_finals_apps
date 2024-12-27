from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    short_id: str
    full_url: str

    class Config:
        orm_mode = True

class URLStats(BaseModel):
    short_id: str
    full_url: str
    visits: int

    class Config:
        orm_mode = True
