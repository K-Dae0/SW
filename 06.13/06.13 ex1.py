'''
2023.06.13
202395005 김대영
# 문제 정의
    사용자로부터 3개의 숫자를 입력받아 가장 큰 수를 구하는 프로그램을 작성
    3개의 숫자를 매개변수로 받아 가장 큰 수를 반환하는 부분을 findMax(a,b,c) 함수로 작성

# 문제 분석
    -변수
        정수1(num1), 정수2(num2), 정수3(num3), 반환 값 저장(biggest_number)
    -수식

# 알고리즘
    1. 함수 findMax 선언
        1.1. a,b,c 중 가장 큰 값 찾기
    2. 정수 3개 입력 받기
    3. 입력받은 findMax를 호출(num1, num2, num3 을 매개변수로)
    4. 리턴받은 가장 큰 값 출력
'''
def findMax(a,b,c) : # 함수 findMax(a,b,c) 정의

    if a > b : # 가장 큰 수를 구하는 기능을 정의
        biggest=a
    
    else :
        biggest=b
    
    if biggest < c :
        biggest=c
    
    return biggest # 가장 큰 값을 반환

num1=int(input("첫 번째 숫자 입력 : "))
num2=int(input("두 번째 숫자 입력 : "))
num3=int(input("세 번째 숫자 입력 : "))

# 함수를 호출학도 return문에 의해 반환되는 값을 변수에 저장
biggest_number=findMax(num1,num2,num3)
print("가장 큰 수는 :",biggest_number)