from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schemas import UserCreateSchema
from ..data.models import User

from .config import Config
from ..app.database import get_db

from ..utils import get_password_hash

router = APIRouter(
    prefix=Config.prefix,
    tags=Config.tags,
    responses={404: {"description": "Not found"}},
)


@router.post("/register", response_model=UserCreateSchema)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"username": db_user.username, "email": db_user.email}


@router.post("/login")
def login_user():
    return {"message": "Login route"}
