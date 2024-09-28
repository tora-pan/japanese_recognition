# this will be a script to seed the db with some initial data (hiragana, katakana, kanji, etc)

# read in data from a csv file to seed the db

import csv
from src.data.models import Card 
from src.app.database import get_db

from sqlalchemy.orm import Session

db: Session = next(get_db())


def seed_hiragana():
    with open("src/utils/data/hiragana.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hiragana = Card(
                kana=row["hiragana"],
                romaji=row["romaji"],
            )
            db.add(hiragana)
        db.commit()


def seed_katakana():
    with open("backend/src/utils/data/katakana.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hiragana = Card(
                kana=row["character"],
                romaji=row["romanization"],
                stroke_count=row["stroke_count"],
                meaning=row["meaning"],
            )
            db.session.add(hiragana)
        db.session.commit()


def seed_kanji():
    with open("backend/src/utils/data/kanji.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hiragana = Card(
                kana=row["character"],
                romaji=row["romanization"],
                stroke_count=row["stroke_count"],
                meaning=row["meaning"],
            )
            db.session.add(hiragana)
        db.session.commit()

seed_hiragana()