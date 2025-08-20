# import sys

# for line in sys.stdin:
# 	print(f'your name is {line}')



from pymongo import MongoClient

# 1. MongoDB 연결
client = MongoClient("localhost", 27017)
db = client["test_db"]
collection = db["customers"]

# 2. 데이터 전체 조회
# for doc in collection.find():
#     print(doc)

for doc in collection.find({"car_type": "파비엠aa"}):
    print(doc)