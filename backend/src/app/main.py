from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..cards.routes import router as card_router
from ..auth.routes import router as login_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://0.0.0.0",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "http://localhost:3001",
    "http://0.0.0.0:3001",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=card_router)
app.include_router(router=login_router)


# @app.get("/cards")
# def get_cards():
#     return {
#         "data": [
#             # list of objects that have all hirgana character and a romaji character
#             {"hiragana": "あ", "romaji": "a"},
#             {"hiragana": "い", "romaji": "i"},
#             {"hiragana": "う", "romaji": "u"},
#             {"hiragana": "え", "romaji": "e"},
#             {"hiragana": "お", "romaji": "o"},
#             {"hiragana": "か", "romaji": "ka"},
#             {"hiragana": "き", "romaji": "ki"},
#             {"hiragana": "く", "romaji": "ku"},
#             {"hiragana": "け", "romaji": "ke"},
#             {"hiragana": "こ", "romaji": "ko"},
#             {"hiragana": "さ", "romaji": "sa"},
#             {"hiragana": "し", "romaji": "shi"},
#             {"hiragana": "す", "romaji": "su"},
#             {"hiragana": "せ", "romaji": "se"},
#             {"hiragana": "そ", "romaji": "so"},
#             {"hiragana": "た", "romaji": "ta"},
#             {"hiragana": "ち", "romaji": "chi"},
#             {"hiragana": "つ", "romaji": "tsu"},
#             {"hiragana": "て", "romaji": "te"},
#             {"hiragana": "と", "romaji": "to"},
#             {"hiragana": "な", "romaji": "na"},
#             {"hiragana": "に", "romaji": "ni"},
#             {"hiragana": "ぬ", "romaji": "nu"},
#             {"hiragana": "ね", "romaji": "ne"},
#             {"hiragana": "の", "romaji": "no"},
#             {"hiragana": "は", "romaji": "ha"},
#             {"hiragana": "ひ", "romaji": "hi"},
#             {"hiragana": "ふ", "romaji": "fu"},
#             {"hiragana": "へ", "romaji": "he"},
#             {"hiragana": "ほ", "romaji": "ho"},
#             {"hiragana": "ま", "romaji": "ma"},
#             {"hiragana": "み", "romaji": "mi"},
#             {"hiragana": "む", "romaji": "mu"},
#             {"hiragana": "め", "romaji": "me"},
#             {"hiragana": "も", "romaji": "mo"},
#             {"hiragana": "や", "romaji": "ya"},
#             {"hiragana": "yi", "romaji": "not used"},
#             {"hiragana": "ゆ", "romaji": "yu"},
#             {"hiragana": "ye", "romaji": "not used"},
#             {"hiragana": "よ", "romaji": "yo"},
#             {"hiragana": "ら", "romaji": "ra"},
#             {"hiragana": "り", "romaji": "ri"},
#             {"hiragana": "る", "romaji": "ru"},
#             {"hiragana": "れ", "romaji": "re"},
#             {"hiragana": "ろ", "romaji": "ro"},
#             {"hiragana": "わ", "romaji": "wa"},
#             {"hiragana": "を", "romaji": "wo"},
#             {"hiragana": "ん", "romaji": "n"},
#         ]
#     }


# @app.post("/")
# def create_item(item: str):
#     return {"item": item}


# @app.post("/cards")
# def create_card(card: dict):

#     return {"card": card}
