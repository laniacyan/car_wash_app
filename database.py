from pymongo import MongoClient

# 클라이언트 연결 (로컬 MongoDB 기준, 포트 27017)
client = MongoClient("mongodb://localhost:27017")

# 사용할 데이터베이스와 컬렉션 선택
db = client["gongbiseo"]       # 데이터베이스 이름
collection = db["customers"]   # 컬렉션 이름

# 다른 파일에서도 쓸 수 있게 export
def get_collection():
    return collection




