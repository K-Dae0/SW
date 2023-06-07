'''
2023.05.31
202395005 김대영
# 문제 정의
    1부터 100사이의 정수 난수 10개를 발생시켜 리스트에 저장하고
    리스트의 가장 큰 값과 작은 값을 출력한 뒤, 리스트 값의 합계와 오름차순으로
    정렬된 리스트를 출력하는 프로그램을 작성

# 문제 분석
    -변수
        10개의난수저장(num)    
    -수식

# 알고리즘
    1.랜덤 모듈 추가
    2.변수 초기화
        num=[]
    3.반복(for)
        for i in range(10) :
            난수 추가
            리스트에 저장
    4.결과 출력(큰값,작은값,합계,오름차순)
'''
import random # random 모듈 사용 선언

num=[] # 비어있는 리스트 num 선언

for i in range(10) : # 10번 반복

    num.append(random.randint(1,100)) # 리스트에 10개의 난수 추가(append)

print("생성된 리스트 :", num)
print("가장 큰 값 :", max(num))
print("가장 작은 값 :", min(num))
print("전체 요소의 합 :", sum(num))
num.sort()
print("정렬된 리스트 :", num)
num.reverse()
print("내림차순된 리스트 :", num)