import time
from fastapi import Depends, HTTPException, Security
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from jwt import PyJWTError as JWTError
import jwt

from passlib.context import CryptContext

from ..data.models import User
from ..app.database import get_db

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security = HTTPBearer(auto_error=False)


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    token = create_access_token(data={"sub": user.email})

    return {"token": token}


def create_access_token(data: dict, expires_delta: timedelta = None, scope: str = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    # if scope:
    #     to_encode.update({"scope": scope})
    # else:
    #     to_encode.update({"scope": "AccessToken"})

    to_encode.update({"exp": expire})
    # to_encode.update({"iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    token: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(get_db),
):
    # if token is None:
    #     print("No token provided")
    #     raise HTTPException(status_code=404, detail="No token provided")

    try:
        payload = jwt.decode(
            token.credentials, SECRET_KEY, algorithms=[ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        if payload["exp"] < time.time():
            raise HTTPException(status_code=401, detail="Token has expired")

        user = db.query(User).filter(User.email == email).first()

        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
