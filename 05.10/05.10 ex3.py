'''
2023.05.09
202395005 김대영
사용자로부터 하나의 숫자를 입력받아 *을 출력하는 프로그램을 구하기
사용자가 7을 입력한 경우 7줄에 *을 하나씩 증가시켜 출력
#문제분석
    -변수
        정수(num)
    -수식

#알고리즘
    1.변수 초기화
        num를 정수로 입력 받기
    2.논리(중첩 반복)
        for i in range(1,num+1)
            for j in range(1,i+1)
'''
num1=int(input("숫자 입력 : "))

for i in range(1,num1+1) :
    for j in range(1,i+1) :
        print("*",end='')        
    print() # 줄 바꿈
    

# 거꾸로 출력
print("\n거꾸로 출력")

num2=int(input("숫자 입력 : "))

for i in range(1,num2+1) :
    for j in range(i,num2+1) :
        print("*",end='')
    print() # 줄 바꿈

