
from pymongo import MongoClient
import random
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']


# 랜덤한 날짜 구하기
    # 수동 데이터
        # 시작, 끝 날짜
def random_yeardate():
    # 시작 날짜와 종료 날짜 설정 (원하는 범위 내에서 날짜를 생성할 수 있도록)
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    # print("start_date : ", start_date)
    # print("end_date : ", end_date)

    # 시작 날짜와 종료 날짜 사이에서 랜덤한 날짜 생성
    # random_day = random.randint(0, (end_date - start_date).days)
    # print("random_days : ", random_day)
    # random_date = start_date + timedelta(days=random_day)
    # print("random_date : ", random_date)
    while True:
        random_day = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_day)

        if random_date.weekday() not in [4, 5]:  # 4: Friday, 5: Saturday
            break

    # return random_date.strftime("%Y년 %m월 %d일")
    return random_date

a = random_yeardate()
print(a)
print(a.weekday())

b = a.strftime("%Y-%m-%d")
print('b = ', b)


# 날짜의 요일 찾기
def get_day_of_week(yeardate):
    yeardate.weekday()
    print(yeardate.weekday())


# 일정 추가 코드

# 세차 일정 추가(미구현)
    # 1. 고객의 id를 받는다.
    # 2. 고객의 해당하는 세차주기를 받는다.
    # 3. 고객의 세차주기에 맞춰 일정을 넣는다.
        # 일정이 같은날 있다면 다시 찾는다.

# 랜덤 세차 일정 추가(미구현)
    # 1. 고객의 id를 받는다.
    # 2. 세차일정을 정한다.
    # 3. 겹치는 일정이 있다면 다시 찾는다.
    # 4. 휴일이 있다면 다시 찾는다.

# 데이터 개수 받기
def input_num():
    while True:
        try:
            num = int(input("몇 개의 데이터를 입력하시겠습니까? "))
            return num
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")

def generate_wash_schedule_data_test(id):
    wash_date = random.choice(['2023-08-01', '2023-08-02', '2023-08-03'])
    wash_type = random.choice(['외부', '내부', '내외부', 'AS세차', '간편세차'])
    unpaid = random.choice([True, False])
    worker = random.choice(['직원1', '직원2', '직원3'])
    wash_amount = random.choice(['5000', '6000', '7000'])
    wash = random.choice(['True', 'False'])

    return {
        'id': id,
        'wash_date': wash_date,
        'wash_type': wash_type,
        'unpaid': unpaid,
        'payment_info': '',
        'worker': worker,
        'wash_amount': wash_amount,
        'wash': wash
    }

# 세차주기 구하기
    # id에 해당하는 고객의 세차주기를 알려준다.
def find_wash_cycle(id):
    collection = db["customers"]
    customer = []

    for doc in collection.find({'id': id}):
        customer.append(doc)
        print('customer : ', customer)

    # print('세차주기 : ', customer[0].get('wash_cycle'))
    return customer[0].get('wash_cycle')


# 고객id를 랜덤하게 정해 지정해준다.
def find_id_test():
    collection = db["customers"]
    list_id = []
    for doc in collection.find():
        list_id.append(doc.get("id"))
    print("list_id : ", list_id)
    id = random.choice(list_id)

    return id

# 데이터 삽입
    # 수동 입력 데이터
    # 1. 넣을 데이터 개수
    # 2. 넣을 고객 정하기
def insert_data_test():
    # 넣을 데이터 개수를 구한다.
    num = input_num()
    
    # 랜덤하게 고객을 정한다.
    id = find_id_test()
    

    
    for i in range(num):
        # 랜덤 데이터 생성
        data = generate_wash_schedule_data_test(id)
        
        # 데이터베이스에 세차 일정 정보 삽입
        db.wash_schedule.insert_one(data)
        print(f"Inserted wash schedule data: {data}")
        
    return 0

    # (['매주', '격주', '월1회', '월세차'])


# insert_data_test()



# 원하는 고객의 다음 세차일
    # wash_plan에 세차일이 모두 적혀있을 것이다.
    # customers - wash_cycle을 확인해 세차주기를 확인.
    # wash_plan - 
    # stop_status - 고객이 세차를 중지했는지 확인한다.
    # 연기했을 경우는 어떻게 하는가?

    # 경우의 수
        # 첫 세차일 경우(기록이 없다)
        # 정상적인 차량의 경우
        # 세차를 중지한 경우
        # 세차를 연기한 경우
        # 세차주기를 변경한 경우
        # 세차일이 휴일인 경우
        # 세차일이 겹치는 경우

    # 1. 고객의 id를 받는다.(구현)
    # 2. 세차기록을 확인해 마지막 세차 진행일을 확인한다.
    # 3. 세차 주기를 확인해 다음 세차일을 확인한다.

def find_next_wash_day(customer_id):
    # 1. 고객을 지정한다.
        # 이미 지정되어있다. (customer_id)
        
    # 2. 고객의 세차기록을 본다.
    collection = db["wash_schedule"]
    list = []
    # 미진행 기록을 전부 가져온다.
    for doc in collection.find({"id": customer_id}):
        if doc.get("wash") == "False":
            list.append(doc)
            
    if len(list) == 0:
        print("미진행 세차 기록이 없습니다.")
        # 3. 고객의 마지막 세차일을 찾는다.
        # 그 바로 다음주기가 고객의 다음 세차일이다.
        # 4. 고객의 세차주기를 본다.
        collection = db["customers"]
        for doc in collection.find({"id": customer_id}):
            wash_cycle = doc.get("wash_cycle")
            print("wash_cycle : ", wash_cycle)
            if wash_cycle == "매주":
                print("다음 세차일은 다음주입니다.")
            elif wash_cycle == "격주":
                print("다음 세차일은 다다음주입니다.")
            elif wash_cycle == "월1회":
                print("다음 세차일은 다음달입니다.")
            else:
                print("오류발생")
                return 0
        # 5. 고객의 다음 세차일을 지정할 수 있다.
            # 3번에서 찾은 값에 일주일을 더한다.
            # 더한 값의 요일이 4, 5가 아니면 알려준다.
                # 4, 5면 알려준다.
    else:
        # 고객의 미진행 세차기록 중 가장 과거의 것을 찾으면 다음 세차일이다.
        return 0
    return 0

# def find_next_wash_day_test():
#     find_next_wash_day(5)

# find_next_wash_day_test()



i = 11
id = 5
collection = db["wash_schedule"]
for doc in collection.find({'id': id}):
    print(doc)





