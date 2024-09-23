from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schemas import CardSchema
from ..data.models import Card

from .config import Config
from ..app.database import get_db

router = APIRouter(
    prefix=Config.prefix,
    tags=Config.tags,
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[CardSchema])
async def get_cards(db: Session = Depends(get_db)):
    all_cards = db.query(Card).all()
    return [CardSchema.model_validate(card).model_dump() for card in all_cards]


@router.post("/", response_model=str)
async def create_card(card: CardSchema, db: Session = Depends(get_db)):
    # create new card
    new_card = Card(
        kana=card.kana,
        romaji=card.romaji,
        stroke_count=card.stroke_count,
        meaning=card.meaning,
        example_word=card.example_word,
    )
    db.add(new_card)
    db.commit()
    db.refresh(new_card)

    return f"Card {new_card.kana} created successfully"
