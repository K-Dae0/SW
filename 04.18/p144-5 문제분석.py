'''
2023.04.18
202395005 김대영
두 개의 숫자를 입력받아 두 번째 수가 첫 번째 수의 약수인지 구분하는 프로그램 구하기
#문제분석
    -변수 
        정수1(num1),정수2(num2)
    -수식
        num1%num2==0
#알고리즘
    1.변수 선언
        num1, num2에 정수로 입력 받기
    2.논리(선택)
    if num1%num2==0 :
        print("{}는 {}의 약수입니다.".format(num2,num1))
    else :
        print("{}는 {}의 약수가아닙니다.".format(num2,num1))
'''
num1=int(input("첫 번째 정수를 입력하세요 : "))
num2=int(input("두 번째 정수를 입력하세요 : "))

if num1%num2==0 :
    print("{}는 {}의 약수입니다.".format(num2,num1)) # 조건이 참일 때 출력
else :
    print("{}는 {}의 약수가아닙니다.".format(num2,num1)) # 조건이 거짓일 때 출력