from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def create_item(item: str):
    print('item:', item)
    return {"item": item}