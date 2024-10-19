from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .schemas import LoginSchema, UserCreateSchema, UserResponseSchema
from ..data.models import User

from .config import Config
from ..app.database import get_db

from ..utils.auth import authenticate_user, get_current_user, get_password_hash

router = APIRouter(
    prefix=Config.prefix,
    tags=Config.tags,
    responses={404: {"description": "Not found"}},
)


@router.post("/register", response_model=UserResponseSchema)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username, email=user.email, password_hash=hashed_password
    )

    # Conditionally add optional fields
    if user.first_name:
        db_user.first_name = user.first_name
    if user.last_name:
        db_user.last_name = user.last_name

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"username": db_user.username, "email": db_user.email}


@router.post("/login")
def login_user(user: LoginSchema, db: Session = Depends(get_db)):
    return authenticate_user(email=user.email, password=user.password, db=db)


@router.get("/me", response_model=UserResponseSchema)
def read_user_me(
    credentials: Annotated[UserResponseSchema, Depends(get_current_user)]
):
    print(credentials.__dict__)
    return credentials
