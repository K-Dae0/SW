'''
2023.04.19
202395005 김대영
조건문을 사용하여 입력된 수가 양수,0,음수인지 판별하는 프로그램을 
두가지 형태인 단순 if문 형태와 이중 if문 형태로 작성하기
#문제분석
    -변수 
        정수(num)
#알고리즘
    1.변수 선언
        num에 정수로 입력 받기
    2.논리(선택)
    -단순 if문
        if num > 0 :
            "양수"
        if num < 0 :
            "음수"
        if num == 0 :
            "0"

    -이중 if문
        if num > 0 :
            "양수"
        elif num < 0 :
            "음수"
        else :
            "0"
'''
# 단순 if문
num=int(input("숫자 입력 : "))

if num > 0 :
    print("입력값 {}은(는) 양수입니다.".format(num))

if num < 0 :
    print("입력값 {}은(는) 음수입니다.".format(num))

if num == 0 :
    print("입력값 {}은 0입니다.".format(num))

# 이중 if문
num=int(input("숫자 입력 : "))

if num > 0 :
    print("입력값 {}은(는) 양수입니다.".format(num))

elif num < 0 :
    print("입력값 {}은(는) 음수입니다.".format(num))

else:
    print("입력값 {}은 0입니다.".format(num))