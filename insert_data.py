# 데이터 삽입 함수 만들기
# 1. 숫자를 입력받는다.
# 2. 데이터를 랜덤하게 생성한다.
# 3. 입력받은 숫자만큼 랜덤한 데이터를 생성해 넣는다.

# 문제점 1. 2번 데이터를 넣으면 id가 중복된다.

# 완성품 1
    # from pymongo import MongoClient
    # import random

    # client = MongoClient('mongodb://localhost:27017/')
    # db = client['test_db']

    # # 사용할 전역변수
    # wash_location = []
    # car_number = int()
    # car_type = []
    # parking_location = int()
    # parking_floor = []
    # parking_time = int()
    # payment_method = []
    # wash_cycle = []
    # phone_number1 = int()
    # phone_number2 = int()


    # # 1. 랜덤 데이터 생성
    # def generate_random_data():
    #     global wash_location, car_number, car_type, parking_location, parking_floor, parking_time, wash_cycle, payment_method, phone_number1, phone_number2
    #     wash_location = random.choice(['송도', '롯데', '힐스'])
    #     car_number = random.randint(1000, 9999)
    #     car_type = random.choice(['검볼보', '큰검벤', '검제', '검제네', '파벤', '파비엠', '검비엠', '큰흰벤', '검펠리', '검지바겐', '큰검비엠', '흰디스', '검포르', '흰아우', '회제네', '검벤', '파미니', '녹제네', '파제네', '큰검볼', '검큰비'])
    #     parking_location = random.randint(1000, 1300)
    #     parking_floor = random.choice(['1층', '2층'])
    #     parking_time = random.randint(8, 10)
    #     wash_cycle = random.choice(['매주', '격주', '월1회', '월세차'])
    #     payment_method = random.choice(['선불', '후불', '자동이체'])
    #     phone_number1 = random.randint(1000, 9999)
    #     phone_number2 = random.randint(1000, 9999)

    #     return 0

    # # 2. 데이터 개수 받기
    # def input_num():
    #     while True:
    #         try:
    #             num = int(input("몇 개의 데이터를 입력하시겠습니까? "))
    #             return num
    #         except ValueError:
    #             print("유효한 숫자를 입력해 주세요.")

    # # 3. 데이터 삽입
    # def insert_data():
    #     # 데이터 개수 받기
    #     num = input_num()
    #     for id in range(num):
    #         # 랜덤 데이터 생성
    #         generate_random_data()
    #         customer_data = {
    #             'id': id,
    #             'wash_location': wash_location,
    #             'car_number': car_number,
    #             'car_type': car_type,
    #             'parking_location': parking_location,
    #             'parking_floor': parking_floor,
    #             'parking_time': f"{parking_time}시",
    #             'wash_cycle': wash_cycle,
    #             'payment_method': payment_method,
    #             'phone_number': f"010-{phone_number1}-{phone_number2}",
    #             'car_memo': '',
    #             'memo': '',
    #             'group': ''
    #         }

    #         # 데이터베이스에 고객 정보 삽입
    #         db.customers.insert_one(customer_data)
    #         print(f"Inserted customer data: {customer_data}")
        
    #     return 0

    # insert_data()
# 완성품 2(최종)
    # 메모 미구현상태
from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
# collection = db["customers"]


# 랜덤 데이터 생성
def generate_customer_data(id):
    wash_location = random.choice(['송도', '롯데', '힐스'])
    car_number = random.randint(1000, 9999)
    car_type = random.choice(['검볼보', '큰검벤', '검제', '검제네', '파벤', '파비엠', '검비엠', '큰흰벤', '검펠리', '검지바겐', '큰검비엠', '흰디스', '검포르', '흰아우', '회제네', '검벤', '파미니', '녹제네', '파제네', '큰검볼', '검큰비'])
    parking_location = random.randint(1000, 1300)
    parking_floor = random.choice(['1층', '2층'])
    parking_time = random.randint(8, 10)
    wash_cycle = random.choice(['매주', '격주', '월1회', '월세차'])
    payment_method = random.choice(['선불', '후불', '자동이체'])
    phone_number1 = random.randint(1000, 9999)
    phone_number2 = random.randint(1000, 9999)

    return {
        'id': id,
        'wash_location': wash_location,
        'car_number': car_number,
        'car_type': car_type,
        'parking_location': parking_location,
        'parking_floor': parking_floor,
        'parking_time': f"{parking_time}시",
        'wash_cycle': wash_cycle,
        'payment_method': payment_method,
        'phone_number': f"010-{phone_number1}-{phone_number2}",
        'car_memo': '',
        'memo': '',
        'group': ''
    }

def generate_wash_schedule_data(id):
    wash_date = random.choice(['2023-08-01', '2023-08-02', '2023-08-03'])
    wash_type = random.choice(['외부', '내부', '내외부', 'AS세차', '간편세차'])
    unpaid = random.choice([True, False])
    worker = random.choice(['직원1', '직원2', '직원3'])
    wash_amount = random.choice(['5000', '6000', '7000'])

    return {
        'id': id,
        'wash_date': wash_date,
        'wash_type': wash_type,
        'unpaid': unpaid,
        'payment_info': '',
        'worker': worker,
        'wash_amount': wash_amount
    }

def generate_payments_data(id):
    date = random.choice(['2023-08-01', '2023-08-02', '2023-08-03'])
    amount = random.choice(['45000', '25000', '75000'])
    name = random.choice(['고객1', '고객2', '고객3'])

    return {
        'id': id,
        'date': date,
        'amount': amount,
        'name': name
    }
    
def generate_unknown_payment_data(id):
    date = random.choice(['2023-08-01', '2023-08-02', '2023-08-03'])
    amount = random.choice(['45000', '25000', '75000'])
    name = random.choice(['고객4', '고객5', '고객6'])

    return {
        'id': id,
        'date': date,
        'amount': amount,
        'name': name
    }

def generate_staff_data(id):
    name = random.choice(['직원1', '직원2', '직원3'])
    phone = random.choice(['010-1234-5678', '010-2345-6789', '010-3456-7890'])
    location = random.choice(['위치1', '위치2', '위치3'])
    date_joined = random.choice(['2020-01-01', '2020-02-01', '2020-03-01'])
    level_1 = random.choice(['2020-01-01', '2020-02-01', '2020-03-01'])
    level_2 = random.choice(['2020-01-01', '2020-02-01', '2020-03-01'])
    level_3 = random.choice(['2020-01-01', '2020-02-01', '2020-03-01'])

    return {
        'staff_id': id,
        'name': name,
        'phone_number': phone,
        'location': location,
        'date_joined': date_joined,
        'level_1': level_1,
        'level_2': level_2,
        'level_3': level_3
    }

def generate_memo_data(id):
    return {
        'memo_id': id,
        'memo': '메모 내용'
    }


# 데이터 개수 받기
def input_num():
    while True:
        try:
            num = int(input("몇 개의 데이터를 입력하시겠습니까? "))
            return num
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")

# 콜렉션에서 id를 이용해 검색한다.
def find_id(collection):
    i = 0
    while True:
        doc = db[collection].find_one({"id": i})
        if doc is None:
            return i
        i = i + 1

# 정보 확인
def check_collection():
    collection_map = {'고객정보': 'customers', '세차일정': 'wash_schedule', '입금내역': 'payments', '입금고객': 'unknown_payments', '직원정보': 'staff', '메모': 'memo'}
    while True:
        collection_name = input("어떤 정보를 확인하시겠습니까? (고객정보, 세차일정, 입금내역, 입금고객, 직원정보, 메모) \n")
        if collection_name in collection_map:
            print(collection_map[collection_name])
            return collection_map[collection_name]
        print("유효하지 않은 선택입니다.")

# 데이터 삽입
def insert_data():
    # 넣을 데이터 종류를 구한다.
    collection = check_collection()
    # 넣을 데이터 개수를 구한다.
    num = input_num()
    for i in range(num):
        if collection == 'customers':
            id = find_id(collection)
            # 랜덤 데이터 생성
            data = generate_customer_data(id)
            
            # 데이터베이스에 고객 정보 삽입
            db.customers.insert_one(data)
            print(f"Inserted customer data: {data}")
            
        elif collection == 'wash_schedule':
            id = find_id(collection)
            # 랜덤 데이터 생성
            data = generate_wash_schedule_data(id)
            
            # 데이터베이스에 세차 일정 정보 삽입
            db.wash_schedule.insert_one(data)
            print(f"Inserted wash schedule data: {data}")
        
        elif collection == 'payments':
            id = find_id(collection)
            # 랜덤 데이터 생성
            data = generate_payments_data(id)

            # 데이터베이스에 입금 내역 정보 삽입
            db.payments.insert_one(data)
            print(f"Inserted payments data: {data}")

        elif collection == 'unknown_payments':
            id = find_id(collection)
            # 랜덤 데이터 생성
            data = generate_unknown_payment_data(id)

            # 데이터베이스에 입금 고객 정보 삽입
            db.unknown_payments.insert_one(data)
            print(f"Inserted unknown payments data: {data}")

        elif collection == 'staff':
            id = find_id(collection)
            # 랜덤 데이터 생성
            data = generate_staff_data(id)

            # 데이터베이스에 직원 정보 삽입
            db.staff.insert_one(data)
            print(f"Inserted staff data: {data}")

    return 0

insert_data()









