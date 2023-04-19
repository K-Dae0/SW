'''
2023.04.18
202395005 김대영
두 정수를 입력받아 두 정수의 연산 값이 출력되는 프로그램 구하기
(1)x > y 나눗셈의 몫 출력
   x < y 합 출력
   x == y 곱 출력
#문제분석
    -변수 
        x의 값(num1),y의 값(num2)
#알고리즘
    1.변수 선언
        num1, num2에 정수 입력 받기
    2.논리(선택)
        if num1 > num2 :
            if num2 != 0 :
                print("{}//{}={}".format(num1,num2,num1//num2))
            else :
                print("y의 값이 0입니다.")
        elif num1 < num2 :
            print("{}+{}={}".format(num1,num2,num1+num2))
        else :
            print("{}*{}={}".format(num1,num2,num1*num2))        
'''
num1=int(input("x의 값을 입력해주세요 : "))
num2=int(input("y의 값을 입력해주세요 : "))

if num1 > num2 :
    if num2 != 0 :
        print("{}//{}={}".format(num1,num2,num1//num2)) # y가 0이 아닐 때 출력
    else :
        print("y의 값이 0입니다.") # y가 0일 때 출력
elif num1 < num2 :
    print("{}+{}={}".format(num1,num2,num1+num2))
else :
    print("{}*{}={}".format(num1,num2,num1*num2))


    
    