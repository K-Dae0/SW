'''
2023.04.11
202395005 김대영
정수 2개와 연산자 1개(+,-,*,/)를 입력 받아서 
사칙연산을 수행하는 프로그램 작성
'''
# 정수로 입력
num1=int(input("정수1:"))
num2=int(input("정수2:"))

op=input("연산자:")

if op== "+": # 만약에 연산자가 "+" 일때
    print(num1+num2) # 두 정수를 더한 값을 출력

elif op== "-": # 만약에 연산자가 "-" 일때
    print(num1-num2) # 두 정수를 뺀 값을 출력

elif op== "*": # 만약에 연산자가 "*" 일때
    print(num1*num2) # 두 정수를 곱한 값을 출력

elif op== "/": # 만약에 연산자가 "/" 일때
    print(num1/num2) # 두 정수를 나눈 값을 출력


