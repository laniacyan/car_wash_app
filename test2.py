from pymongo import MongoClient


client = MongoClient("localhost", 27017)
database = client["test_db"]
collection = database["customers"]

database["customers"].insert_one(
{ 'id': '구분을 위한 키값', 'wash_location': '세차장 위치', 'car_number': '차량 번호', 'car_type': '차량 종류', 'parking_location': '입고 위치', 'parking_time': '입고 시간', 'wash_cycle': '세차 주기', 'payment_method': '납부 방식', 'phone_number': '전화번호', 'car_memo': '', 'memo': '메모', 'group': '묶음차량' }
)
database["wash_schedule"].insert_one(
{ 'id': '구분을 위한 키값', 'wash_date': '세차 날짜', 'wash_type': '세차 종류', 'unpaid': 'true/false', 'payment_info': '지불 내역', 'worker': '작업자', 'wash_amount': '직원에게 지급할 액수' }
)
database["payments"].insert_one(
{ 'id': '입금 고객을 구분하기 위한 키값', 'date': '입금 날짜', 'amount': '입금 액수', 'name': '입금자명' }
)
database["unknown_payments"].insert_one(
{ 'date': '입금 날짜', 'amount': '입금 액수', 'name': '입금자명' }
)
database["staff"].insert_one(
{ 'staff_id': '직원 구분을 위한 키값', 'name': '직원 이름', 'phone_number': '직원 전화번호', 'location': '담당위치', 'date_joined': '입사일', 'level_1': '1레벨 날짜', 'level_2': '2레벨 날짜', 'level_3': '3레벨 날짜' }
)
database["memos"].insert_one(
{ 'memo_id': '메모 구분을 위한 키값', 'memo': '메모 내용' }
)
