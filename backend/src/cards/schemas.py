from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProgressSchema(BaseModel):
    review_count: Optional[int] = None
    last_reviewed_at: Optional[datetime] = None
    accuracy: float

    class Config:
        from_attributes = True


class CardSchema(BaseModel):
    id: int
    kana: str
    romaji: str
    stroke_count: Optional[int] = None
    meaning: Optional[str] = None
    example_word: Optional[str] = None
    # progress: Optional[ProgressSchema] = None

    class Config:
        from_attributes = True


class CardUpdateSchema(BaseModel):
    username: str
    progress: ProgressSchema
