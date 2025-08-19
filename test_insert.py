from pymongo import MongoClient

client = MongoClient("localhost", 27017)
database = client["test_db"]


database["customers"].insert_many([
    { 'id': '1', 'wash_location': '송도', 'car_number': '2001', 'car_type': '검볼보', 'parking_location': '1301 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-1234-1234', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '2', 'wash_location': '송도', 'car_number': '2002', 'car_type': '큰검벤', 'parking_location': '1302 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-1234', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '3', 'wash_location': '송도', 'car_number': '3001', 'car_type': '검제', 'parking_location': '1303 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-1234-0000', 'car_memo': '', 'memo': '', 'group': '4' },
    { 'id': '4', 'wash_location': '송도', 'car_number': '3002', 'car_type': '검제네', 'parking_location': '1304 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-5555-0000', 'car_memo': '', 'memo': '', 'group': '3' },
    { 'id': '5', 'wash_location': '송도', 'car_number': '4500', 'car_type': '파벤', 'parking_location': '1304 2층', 'parking_time': '7시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-6666', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '6', 'wash_location': '송도', 'car_number': '4501', 'car_type': '파비엠', 'parking_location': '1303 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-7777-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '7', 'wash_location': '송도', 'car_number': '5502', 'car_type': '검비엠', 'parking_location': '1302 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-8888-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '8', 'wash_location': '송도', 'car_number': '5546', 'car_type': '큰흰벤', 'parking_location': '1301 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-9999', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '9', 'wash_location': '롯데', 'car_number': '1101', 'car_type': '검펠리', 'parking_location': '2202 1층', 'parking_time': '9시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '10', 'wash_location': '롯데', 'car_number': '1201', 'car_type': '검지바겐', 'parking_location': '2202 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '11', 'wash_location': '롯데', 'car_number': '1103', 'car_type': '큰검비엠', 'parking_location': '2202 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '12', 'wash_location': '롯데', 'car_number': '2203', 'car_type': '흰디스', 'parking_location': '2203 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '13', 'wash_location': '롯데', 'car_number': '7706', 'car_type': '검포르', 'parking_location': '2204 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '월1회', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '14', 'wash_location': '롯데', 'car_number': '7540', 'car_type': '흰아우', 'parking_location': '2202 2층', 'parking_time': '7시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '15', 'wash_location': '롯데', 'car_number': '8239', 'car_type': '회제네', 'parking_location': '2201 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '16', 'wash_location': '힐스', 'car_number': '8860', 'car_type': '검벤', 'parking_location': '2403 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '17', 'wash_location': '힐스', 'car_number': '9293', 'car_type': '파미니', 'parking_location': '2403 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '18', 'wash_location': '힐스', 'car_number': '9911', 'car_type': '녹제네', 'parking_location': '2402 2층', 'parking_time': '9시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '19', 'wash_location': '힐스', 'car_number': '1234', 'car_type': '파제네', 'parking_location': '2409 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '20', 'wash_location': '힐스', 'car_number': '7777', 'car_type': '큰검볼', 'parking_location': '2406 1층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '격주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
    { 'id': '21', 'wash_location': '힐스', 'car_number': '5555', 'car_type': '검큰비', 'parking_location': '2401 2층', 'parking_time': '8시', 'wash_cycle': '', 'payment_method': '매주', 'phone_number': '010-0000-0000', 'car_memo': '', 'memo': '', 'group': '' },
])
# database["wash_schedule"].insert_one(
# { 'id': '구분을 위한 키값', 'wash_date': '세차 날짜', 'wash_type': '세차 종류', 'unpaid': 'true/false', 'payment_info': '지불 내역', 'worker': '작업자', 'wash_amount': '직원에게 지급할 액수' }
# )
# database["payments"].insert_one(
# { 'id': '입금 고객을 구분하기 위한 키값', 'date': '입금 날짜', 'amount': '입금 액수', 'name': '입금자명' }
# )
# database["unknown_payments"].insert_one(
# { 'date': '입금 날짜', 'amount': '입금 액수', 'name': '입금자명' }
# )
# database["staff"].insert_one(
# { 'staff_id': '직원 구분을 위한 키값', 'name': '직원 이름', 'phone_number': '직원 전화번호', 'location': '담당위치', 'date_joined': '입사일', 'level_1': '1레벨 날짜', 'level_2': '2레벨 날짜', 'level_3': '3레벨 날짜' }
# )
# database["memos"].insert_one(
# { 'memo_id': '메모 구분을 위한 키값', 'memo': '메모 내용' }
# )
