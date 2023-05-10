'''
2023.05.09
202395005 김대영
하나의 숫자를 입력받아 팩토리얼을 구하는 프로그램을 for문을 사용하여 작성하기
#문제분석
    -변수
        정수(num) , 팩토리얼(fac)
    -수식
        n! = n * (n-1) * (n-2).... * 1
#알고리즘
    1.변수 선언
        num을 정수로 입력 받기
    2.논리(반복)
        fac=1
        for i in range(num,0,-1) :
        
            fac=fac * i
        
        print(팩토리얼의 값)
'''
num=int(input("팩토리얼 숫자 입력 : "))

fac=1 # 0이 아닌 1로 초기화

for i in range(num,0,-1) :

    # range() 함수를 사용하여 입력된 숫자부터 1까지 1씩 감소시키며 반복 수행
    fac = fac * i

print("%d의 팩토리얼 값은 : "%num,fac) # %d에서의 d는 정수를 의미 , %f는 실수