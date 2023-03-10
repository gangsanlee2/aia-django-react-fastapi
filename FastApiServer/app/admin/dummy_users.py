import datetime
import random
import string
from datetime import timedelta, datetime

import pandas as pd
import shortuuid
from passlib.context import CryptContext
from sqlalchemy import create_engine

lambda_string = lambda k: ''.join(random.sample(string.ascii_lowercase, k))
random_number = lambda start, end: random.randrange(start, end)
lambda_number = lambda k: ''.join(str(random_number(0, 10)) for _ in range(k))
lambda_time = lambda x: datetime.datetime.now().strftime(x) # '%Y-%m-%d %H:%M:%S'
first_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권"]
name_words = ["가", "강", "건", "경", "고", "관", "광", "구", "규", "근", "기", "길", "나", "남", "노", "누", "다", "단", "달",
              "담", "대", "덕", "도", "동", "두", "라", "래", "로", "루", "리", "마", "만", "명", "무", "문", "미", "민", "바",
              "박", "백", "범", "별", "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", "설", "섭", "성", "세", "소",
              "솔", "수", "숙", "순", "숭", "슬", "승", "시", "신", "아", "안", "애", "엄", "여", "연", "영", "예", "오", "옥",
              "완", "요", "용", "우", "원", "월", "위", "유", "윤", "율", "으", "은", "의", "이", "익", "인", "일", "잎", "자",
              "잔", "장", "재", "전", "정", "제", "조", "종", "주", "준", "중", "지", "진", "찬", "창", "채", "천", "철", "초",
              "춘", "충", "치", "탐", "태", "택", "판", "하", "한", "해", "혁", "현", "형", "혜", "호", "홍", "화", "환", "회",
              "효", "훈", "휘", "희", "운", "모", "배", "부", "림", "봉", "혼", "황", "량", "린", "을", "비", "솜", "공", "면",
              "탁", "온", "디", "항", "후", "려", "균", "묵", "송", "욱", "휴", "언", "령", "섬", "들", "견", "추", "걸", "삼",
              "열", "웅", "분", "변", "양", "출", "타", "흥", "겸", "곤", "번", "식", "란", "더", "손", "술", "훔", "반", "빈",
              "실", "직", "흠", "흔", "악", "람", "권", "복", "심", "헌", "엽", "학", "개", "롱", "평", "늘", "늬", "랑", "얀", "향",
              "울", "련"]
lambda_k_name = lambda k: ''.join(random.sample(first_names, k-1))+''.join(random.sample(name_words, k))
lambda_phone = lambda k: '010-'+str(lambda_number(k))+'-'+str(lambda_number(k))
lambda_birth = lambda startyear, endyear: str(random_number(startyear,endyear))+'-'+str(random_number(1,12))+'-'+str(random_number(1,32))
lambda_birth_ohne_ = lambda startyear, endyear: str(random_number(startyear,endyear))+str(random_number(1,12))+str(random_number(1,32))
address_list = ["서울","경기","부산","대구","광주"]
job_list = ["회사원","사업가","개발자","자영업자"]
interests_list = ["영화","주식","부동산","독서"]

class UserService(object):
    def __init__(self):
        global engine, input_password
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        input_password = "12qw"

    def create_user(self) -> []:
        user_id = shortuuid.ShortUUID(alphabet=string.ascii_lowercase + string.digits).random(length=8)
        user_email = str(lambda_string(4)) + "@test.com"
        password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(input_password)     # 백엔드에서 실행할 경우 pip install bcrypt 필요
        user_name = lambda_k_name(2)
        phone = lambda_phone(4)
        birth = lambda_birth_ohne_(1985, 2011)
        address = random.choice(address_list)
        job = random.choice(job_list)
        user_interests = random.choice(interests_list)
        created_at = (datetime.utcnow() + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")
        updated_at = (datetime.utcnow() + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")
        return user_id, user_email, password, user_name, phone, birth, address, job, user_interests, created_at, updated_at

    def create_users(self) -> []:
        rows = [self.create_user() for i in range(100)]
        columns = ['user_id', 'user_email', 'password', 'user_name', 'phone', 'birth', 'address', 'job', 'user_interests', 'created_at', 'updated_at']
        df = pd.DataFrame(rows, columns=columns)
        df['user_email'] = df['user_email'].astype(str)
        return df

    def insert_users(self):
        df = self.create_users()
        df.to_sql(name='users',
                  if_exists='append',
                  con=engine,
                  index=False)

if __name__ == '__main__':
    UserService().insert_users()