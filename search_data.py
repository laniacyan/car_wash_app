# 데이터 검색 함수 만들기.
# 1. 검색할 필드를 입력한다.
# 2. 무엇으로 검색을 할 것인지 정한다.
# 3. 검색할 값을 입력한다.
# 4. 입력된 값에 알맞은 데이터를 보여준다.


from pymongo import MongoClient

# 1. MongoDB 연결
client = MongoClient("localhost", 27017)
db = client["test_db"]

# 2. 데이터 전체 조회
# for doc in collection.find():
#     print(doc)

# for doc in collection.find({"car_type": "파비엠"}):
#     print(doc)


# 정보 확인
def check_collection():
    collection_map = {'고객정보': 'customers', '세차일정': 'wash_schedule', '입금내역': 'payments', '입금고객': 'unknown_payments', '직원정보': 'staff', '메모': 'memos'}
    while True:
        collection_name = input("어떤 정보를 확인하시겠습니까? (고객정보, 세차일정, 입금내역, 입금고객, 직원정보, 메모) \n")
        if collection_name in collection_map:
            print(collection_map[collection_name])
            return collection_map[collection_name]
        print("check_collection 잘못입력함.")
        continue

def select_collection():
    # 검색할 콜렉션을 선택한다.
    collection = check_collection()
    if collection == 'customers':
        field_list = ['id', 'wash_location', 'car_number', 'car_type', 'parking_location', 'parking_floor', 'parking_time', 'wash_cycle', 'payment_method', 'phone_number', 'car_memo', 'memo', 'group']
    elif collection == 'wash_schedule':
        field_list = ['id', 'wash_date', 'wash_type', 'unpaid', 'payment_info', 'worker', 'wash_amount']
    elif collection == 'payments':
        field_list = ['id', 'date', 'amount', 'name']
    elif collection == 'unknown_payments':
        field_list = ['date', 'amount', 'name']
    elif collection == 'staff':
        field_list = ['staff_id', 'name', 'phone_number', 'location', 'date_joined']
    elif collection == 'memos':
        field_list = ['memo_id', 'memo']
    else:
        print("select_collection 잘못입력함.")
        return 0


    return collection, field_list

# 입력한 값이 들어간 모든 데이터를 검색
def search_field_data1(users_field, collection):
    data_list = []
    for field in users_field:
        value = input(f"{field}의 검색어를 입력하세요 \n")
        for doc in db[collection].find({field: value}):
            if doc not in data_list:
                data_list.append(doc)
            # print(doc)
    for data in data_list:
        print(data)

# 입력한 값을 모두 포함한 데이터만 검색
def search_field_data2(users_field, collection):
    main_data_list = []
    search_data_list = []
    i = 0
    for field in users_field:
        value = input(f"{field}의 검색어를 입력하세요 \n")
        for doc in db[collection].find({field: value}):
            # 첫 field 데이터는 다 넣는다.
            if i == 0:
                main_data_list.append(doc)
            # 두번째 이후 데이터는 입력한 값이 모두 일치하면 넣는다.
            else:
                if doc in main_data_list:
                    search_data_list.append(doc)
            # print(doc)
        i = i + 1
        if i > 1:
            main_data_list = search_data_list
        
        # 1. 메인에 데이터를 넣는다.
        # 2. 메인 데이터중 이쁜 데이터만 서치 데이터에 넣는다.
        # 3. 서치 데이터를 메인 데이터에 넣는다.
        # 4. 2번 과정을 다시 진행한다.
        # 5. 2번을 더이상 진행하지 못할 경우 완성본이다.

    for data in main_data_list:
        print(data)
    

# 검색할 컬렉션 및 필드를 입력받는다.
def check_datas():
    collection, field_list = select_collection()
    if collection == 0:
        print('무언가 잘못됨')
        return 0
    users_field = []
    
    while True:
        data_type = input("원하는 정보를 선택하세요. (모든 정보 출력, 직접 입력, 필드 입력) \n")
        if data_type == '모든 정보 출력':
            for doc in db[collection].find():
                print(doc)
            
            print('모든 정보 출력 완료')    
            return 0
                
        elif data_type == '직접 입력':
            value = input("검색: ")
            for field in field_list:
                for doc in db[collection].find({field: value}):
                    print(doc)
                    
            print('검색 결과 출력 완료')
            return 0

        elif data_type == '필드 입력':
            while True:
                print("입력가능 필드 목록:", field_list, '\n')
                print('현재 필드 목록:', users_field)
                user_input = input('1. 필드를 추가한다. 2. 필드를 제거한다. 3. 검색한다.  or 아무키나 입력해 종료. \n')
                if user_input == '1':
                    field = input("추가할 필드를 입력하세요: ")
                    if field in field_list:
                        users_field.append(field)
                    else:
                        print("유효하지 않은 필드입니다.")

                elif user_input == '2':
                    field = input("제거할 필드를 입력하세요: ")
                    if field in users_field:
                        users_field.remove(field)
                    else:
                        print("없는 필드입니다.")
                    
                elif user_input == '3':
                    answer = input("어떻게 검색하시겠습니까? \n\n 1. 입력값 중 하나라도 일치 \n 2. 입력값 모두 일치 3. 돌아간다 \n")
                    if answer == '1':
                        # 입력한 값이 들어간 모든 데이터를 검색
                        search_field_data1(users_field, collection)
                    elif answer == '2':
                        # 입력한 값을 모두 포함한 데이터만 검색
                        search_field_data2(users_field, collection)
                    elif answer == '3':
                        continue
                    else:
                        print("유효하지 않은 선택입니다.")
                else:
                    print("검색 안함.")
                    return 0
        else:
            print("너 잘못입력함.")
            continue
    print('check_datas문제임')
    return 0


check_datas()

