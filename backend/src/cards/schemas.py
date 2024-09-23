from typing import Optional

from pydantic import BaseModel


class CardSchema(BaseModel):
    kana: str
    romaji: str
    stroke_count: int
    meaning:Optional[str] = None
    example_word: Optional[str] = None
    class Config:
        from_attributes = True
