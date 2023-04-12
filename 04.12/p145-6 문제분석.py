'''
2023.04.12
202395005 김대영
두 개의 숫자를 입력 후
모두 짝수이면 두 수를 더한 결과를 출력
둘 중 하나가 홀수이면 몇 번째 입력한 수를 짝수로 입력해야 하는지 출력

#문제분석
    -변수 
        숫자1(num1) , 숫자2(num2)
    -수식
        num1%2==0 (num1은 짝수)
        num1%2==1 (num1은 홀수)
#알고리즘
    1.변수 선언
        -num1 , num2에 정수로 입력
    2.논리(선택 if-elif-else)
        if num1%2==0 and num2%2==0 :
            print("{}+{}={}".format(num1,num2,num1+num2))

        elif num1%2==1 and num2%2==0 :
            print("첫 번째 정수를 짝수로 입력하세요.")

        elif num1%2==0 and num2%2==1 :
            print(두 번째 정수를 짝수로 입력하세요.")

        else :
            print("두 숫자 모두를 짝수로 입력하세요.")     
'''
num1=int(input("첫 번째 정수를 입력하세요 : ")) # num1을 정수로 입력
num2=int(input("두 번째 정수를 입력하세요 : ")) # num2을 정수로 입력

if num1%2==0 and num2%2==0 : # 조건이 참일 때 출력
    print("{}+{}={}".format(num1,num2,num1+num2))

elif num1%2==1 and num2%2==0 : # 조건이 참일 때 출력
    print("첫 번째 정수를 짝수로 입력하세요.")

elif num1%2==0 and num2%2==1 : # 조건이 참일 때 출력
    print("두 번째 정수를 짝수로 입력하세요.")

else : # 조건이 거짓일 때 출력
    print("두 숫자 모두를 짝수로 입력하세요.")



