# 고객의 다음 세차일
# 고객의 마지막 입금일


from pymongo import MongoClient
import random

# 1. MongoDB 연결
client = MongoClient("localhost", 27017)
db = client["test_db"]

# 2. 데이터 전체 조회
# for doc in collection.find():
#     print(doc)

# for doc in collection.find({"car_type": "파비엠"}):
#     print(doc)
















