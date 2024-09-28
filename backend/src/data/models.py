from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


# User model
class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, nullable=False, unique=True)
    password_hash = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False, unique=True)
    created_at = mapped_column(DateTime, server_default=func.now())

    # Relationship to track user progress
    progress = relationship("UserCardProgress", back_populates="user")


# Card model
class Card(Base):
    __tablename__ = "cards"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    kana = mapped_column(String, nullable=False)
    romaji = mapped_column(String, nullable=False)
    stroke_count = mapped_column(Integer, nullable=True)
    meaning = mapped_column(String, nullable=True)
    example_word = mapped_column(String, nullable=True)

    # Relationship for users' progress with this card
    progress = relationship("UserCardProgress", back_populates="card")


# Progress model (tracking user's progress on each card)
class UserCardProgress(Base):
    __tablename__ = "user_card_progress"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    card_id = mapped_column(Integer, ForeignKey("cards.id"), nullable=False)
    last_reviewed_at = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )  # Tracks last review time
    review_count = mapped_column(Integer, default=0)  # Number of times reviewed
    accuracy = mapped_column(Float, default=0.0)  # Score for accuracy in strokes

    # Relationships
    user = relationship("User", back_populates="progress")
    card = relationship("Card", back_populates="progress")
