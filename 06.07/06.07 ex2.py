'''
2023.06.07
202395005 김대영
# 문제 정의
    중복을 허용하지 않는 세트를 이용하여 로또넘버(1~45 사이의 정수) 6개를 오름차순으로
    정렬하여 출력하는 프로그램을 작성, 난수를 사용하고, 1부터의 45사이의 정수 난수를
    구하는 메소드로는 random.randint(1,45)를 사용

# 문제 분석
    -변수
        랜덤세트저장1(lotto)
    -수식

# 알고리즘
    1. 랜덤 모듈 추가
    2. 비어있는 세트 변수 생성
    3. 반복(무한 반복)
        while True :
            lotto변수에 랜덤 수 6개 추가(1~45)

            if len(lotto) == 6 :
                반복을 종료
        
        생성된 번호를 출력
        중복된 수 출력
            
'''
import random # 랜덤 모듈 추가

lotto=set() # 비어있는 세트 변수 생성
cnt=0 # 중복된 숫자를 체크하기 위한 변수

while True : # 무한 반복
    lotto.add(random.randint(1,45)) # 1에서 45사이의 랜덤 수 추가
    cnt=cnt+1 # 난수가 발생할 때 마다 1씩 증가

    if len(lotto) == 6 :
        break

print("이번주 로또 넘버 :",sorted(lotto)) # 오름차순으로 정렬하여 출력
print("중복된 난수의 발생 횟수 : ",cnt-6) # 중복 횟수 출력