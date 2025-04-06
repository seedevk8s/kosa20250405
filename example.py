# pandas는 표 형식의 데이터를 다루기 쉽게 해주는 라이브러리입니다.
import pandas as pd

# random은 무작위 숫자나 문자를 생성할 수 있게 해주는 라이브러리입니다.
import random

# 한국 이름 10명을 리스트로 미리 준비합니다.
names = ["김민수", "이서준", "박지훈", "최예린", "정하늘", "조민지", "장우진", "한소영", "윤지아", "오세훈"]

# 실제 존재하는 시/도/군 조합 10개를 튜플 형식으로 리스트에 저장합니다.
cities = [
    ("서울특별시", "강남구"),
    ("부산광역시", "해운대구"),
    ("대구광역시", "수성구"),
    ("인천광역시", "연수구"),
    ("광주광역시", "동구"),
    ("대전광역시", "서구"),
    ("울산광역시", "남구"),
    ("경기도", "성남시 분당구"),
    ("강원도", "춘천시"),
    ("충청북도", "청주시 상당구")
]

# 이메일 주소를 생성하는 함수입니다.
def generate_email(name):
    # 이메일 앞부분에 들어갈 영문자 6개를 무작위로 생성합니다.
    user_part = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
    
    # 이메일 도메인 중 하나를 무작위로 선택합니다.
    domains = ["gmail.com", "naver.com", "daum.net", "kakao.com"]
    
    # 이메일 주소 형식으로 합쳐서 반환합니다.
    return f"{user_part}@{random.choice(domains)}"

# 최종 데이터를 담을 리스트입니다.
data = []

# 10개의 계정 정보를 만듭니다.
for i in range(10):
    name = names[i]  # 이름 선택
    age = random.randint(20, 50)  # 나이는 20세에서 50세 사이에서 무작위 선택
    email = generate_email(name)  # 이메일 생성
    city, district = cities[i]  # 주소에서 시와 구 선택
    address = f"{city} {district}"  # 전체 주소 문자열로 만들기
    data.append([name, age, email, address])  # 하나의 계정 정보를 리스트에 추가

# pandas DataFrame으로 데이터를 표 형태로 정리합니다.
df = pd.DataFrame(data, columns=["이름", "나이", "이메일", "주소"])

# 파일을 저장할 경로입니다.
file_path = "data.csv"

# CSV 파일로 저장합니다. index=False는 인덱스 번호를 저장하지 않겠다는 의미입니다.
df.to_csv(file_path, index=False)

# 저장된 파일 경로를 출력합니다.
file_path
