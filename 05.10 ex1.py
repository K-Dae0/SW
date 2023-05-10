'''
2023.05.09
202395005 김대영
하나의 숫자를 입력받은 숫자가 소수인지 여부를 출력하는 프로그램을 구하기
#문제분석
    -변수
        정수(num)
    -수식

#알고리즘
    1.변수 초기화
        num을 정수로 입력 받기

    2.논리(반복안에 선택포함)
        for i in range(2,num+1) :
            if num % i == 0 :
                break
        if num == i :
            print(소수)
        
        else :
            print(소수가 아니다)
        print(감사합니다)
'''
num=int(input("소수 검증 숫자 입력 : "))

for i in range(2,num+1) : # 2부터 입력된 숫자까지 반복
    if num % i == 0 :
        break # 나머지가 0이면 반복을 종료

if num == i :
    print("소수입니다")

else :
    print("소수가 아닙니다")
print("소수 판별 프로그램을 이용해주셔서 감사합니다")