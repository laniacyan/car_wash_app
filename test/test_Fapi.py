from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World!!"}

# fake_items_db = [{"item": "Foo"}, {"item": "Bar"}, {"item": "Baz"}]

# @app.get("/items/{item_id}")
# def read_item(item_id: str, skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

@app.get("/")
def home():
    return {"hello": "get"}

@app.post("/")
def home_post(msg: str):
    return {"hello": "post", "msg": msg}
