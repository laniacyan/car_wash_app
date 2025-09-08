


# print('hello, world!')

import sys
from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=1000)
    client.admin.command('ping')
    print("✅ MongoDB 서버 실행 중입니다!")
except Exception as e:
    print("❌ MongoDB 서버가 실행되고 있지 않거나 연결할 수 없습니다.")



# conn_default = MongoClient()

# print(conn_default)

# MongoClient(host='localhost', port=27017, document_class=dict, tz_aware=False, connect=True)



