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
async def get_cards(db: Session = Depends(get_db), user=Depends(get_current_user)):
    all_cards = db.query(Card).all()
    return [CardSchema.model_validate(card).model_dump() for card in all_cards]


@router.post("/", response_model=str)
async def create_card(card: CardSchema, db: Session = Depends(get_db), user=Depends(get_current_user)):
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
    
    progress = (
        db.query(UserCardProgress)
        .filter(
            UserCardProgress.username == user.username,
            UserCardProgress.card_id == card_id,
        )
        .first()
    )

    if not progress:
        prog = UserCardProgress(
            username=updated_card.username,
            card_id=card_id,

        )
        db.add(prog)
        db.commit()
        db.refresh(prog)
        return f"Card progress created"

    progress.review_count += 1
    progress.last_reviewed_at = datetime.utcnow()
    progress.accuracy = updated_card.progress.accuracy or progress.accuracy
    db.commit()
    db.refresh(progress)
    return f"Card progress updated"
