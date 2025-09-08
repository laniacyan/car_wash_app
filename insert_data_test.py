
from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']


def generate_wash_schedule_data():
    wash_date = random.choice(['2023-08-01', '2023-08-02', '2023-08-03'])
    wash_type = random.choice(['외부', '내부', '내외부', 'AS세차', '간편세차'])
    unpaid = random.choice([True, False])
    worker = random.choice(['직원1', '직원2', '직원3'])
    wash_amount = random.choice(['5000', '6000', '7000'])
    wash = random.choice(['True', 'False'])

    return {
        'wash_date': wash_date,
        'wash_type': wash_type,
        'unpaid': unpaid,
        'payment_info': '',
        'worker': worker,
        'wash_amount': wash_amount,
        'wash': wash
    }

def check_id(collection):
    i = 0
    while True:
        doc = db[collection].find_one({"id": i})
        if doc is None:
            return i
        i = i + 1

# 고객id를 랜덤하게 정해 지정해준다.
# def find_id(id):
#     collection = db["customers"]
#     for i in collection.find({"id": id}):
#         print(i)
#     # i = collection.find({"id": id})
#     # print(i)

    
#     # for i in collection.find({"id": id}):
#     #     print(i)
#         # i = i + 1
#     # id = random.randint(0, i-1)
#     return id

def find_id():
    collection = db["customers"]
    list_id = []
    for doc in collection.find():
        list_id.append(doc.get("id"))
    print("list_id : ", list_id)
    id = random.choice(list_id)

    return id

def insert_data():
    # 넣을 데이터 종류를 구한다.
    collection = {'세차일정': 'wash_schedule'}
    # 넣을 데이터 개수를 구한다.
    num = 1
    for i in range(num):
        id = find_id()
        print("\nid = ", id)
        # 랜덤 데이터 생성
        # data = generate_wash_schedule_data()
        
        # # 데이터베이스에 세차 일정 정보 삽입
        # db.wash_schedule.insert_one(data)
        # print(f"Inserted wash schedule data: {data}")




insert_data()
