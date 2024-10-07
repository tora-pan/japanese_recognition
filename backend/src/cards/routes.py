from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..utils.auth import get_current_user

from .schemas import CardSchema, CardUpdateSchema, ProgressSchema
from ..data.models import Card, UserCardProgress

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


@router.put("/progress/{card_id}", response_model=str)
async def update_card_progress(
    card_id: int,
    updated_card: CardUpdateSchema,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    card = db.query(Card).filter(Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    if not card.progress:
        card.progress = UserCardProgress(
            user_id=user.id,
            card_id=card.id,
        )
        db.add(card.progress)
        db.commit()

    card.progress.review_count += 1
    db.commit()
    db.refresh(card.progress)
    return f"Card {card.kana} progress updated"
