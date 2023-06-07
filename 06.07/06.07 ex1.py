'''
2023.06.07
202395005 김대영
# 문제 정의
    1부터 100사이 10개의 랜덤 세트 2개를 생성하고, 두 세트의 합집합, 교집합, 차집합을
    구하는 프로그램을 작성, 난수를 발생하기 위해 랜덤 모듈을 사용하며 프로그램의 처음에
    import random을 포함

# 문제 분석
    -변수
        랜덤세트저장1(num1), 랜덤세트저장2(num2)
    -수식

# 알고리즘
    1. 랜덤 모듈 추가
    2. 비어있는 세트 변수 생성
    3. 반복(무한 반복)
        while True :
            
            if len(num1) < 10 :
                num1에 랜덤 수 추가
            if len(num2) < 10 :
                num2에 랜덤 수 추가

        합집합, 교집합, 차집합 구하기
'''
import random # 랜덤 모듈 추가

num1=set() # 비어 있는 세트 생성
num2=set()

while True : # 무한 반복
    
    if len(num1) < 10 :
        num1.add(random.randint(1,100)) # 1부터 100사이의 랜덤 수 추가
    
    if len(num2) < 10 :
        num2.add(random.randint(1,100))

    if len(num1) == 10 and len(num2) == 10 :
        break # num1, num2가 10개의 난수가 완성되면 반복을 종료

print("발생된 10개의 난수 :",num1)
print("발생된 10개의 난수 :",num2)

print("num1, num2의 합세트 :",num1 | num2) # num1과 num2의 합집합 출력
print("num1, num2의 교세트 :",num1 & num2) # num1과 num2의 교집합 출력
print("num1, num2의 차세트 :",num1 - num2) # num1과 num2의 차집합 출력

