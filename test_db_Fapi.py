# from fastapi import FastAPI
# from fastapi.responses import FileResponse

# from pymongo import MongoClient

# # 1. MongoDB 연결
# client = MongoClient("localhost", 27017)
# db = client["test_db"]
# collection = db["customers"]

# # # 2. 데이터 전체 조회
# # for doc in collection.find():
# #     print(doc)


# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # @app.get('/')
# # def load_html():
# #     return FileResponse("test.html")

# @app.get('/items/{item_id}')
# def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get('/customers/{item_id}')
# def read_customer(item_id: int):
#     customer = collection.find_one({"id": int(item_id)})
#     if customer:
#         return customer
#     return {"error": "Customer not found"}

# # HTTP 422에러
# @app.get('/customers/find')
# def find_customers():
#     doc = collection.find()
#     return doc

##########

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_collection

app = FastAPI()
collection = get_collection()  # MongoDB 컬렉션 가져오기

# 데이터 구조 정의 (요청 바디용)
class Customer(BaseModel):
    name: str
    age: int

@app.post("/add-customer")
async def add_customer(customer: Customer):
    try:
        result = collection.insert_one(customer.dict())
        return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/customers")
async def list_customers():
    data = list(collection.find({}, {"_id": 0}))  # _id는 제외
    return {"customers": data}






