from datetime import datetime, timezone
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import computed_field

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    published_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    content: str

    @computed_field
    @property
    def formatted_date(self):
        return self.published_at.strftime("%d.%m.%Y")

app = FastAPI()

@app.route("/blogs/create")
async def create_a_blog():
    pass