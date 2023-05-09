'''
2023.05.09
202395005 김대영
1부터 1000까지의 정수 중에서 사용자가 입력한 숫자의 배수만을 더하여 출력하는 프로그램 구하기
#문제분석
    -변수
        정수(num) , 합계(total)
    -수식
        
#알고리즘
    1.변수 선언
        num을 정수로 입력 받기
        total=0

    2.논리(반복)
        total=0
        for i in range(num,1001,num) :
            
            total = total + i
        
        print(배수의 합)
'''
num=int(input("합을 원하는 배수 입력 : "))
total=0

for i in range(num,1001,num) :

    #range() 함수를 사용하여 배수로부터 배수만큼씩 증가시키면서 반복
    total = total + i

print("1부터 1000까지 {}의 배수의 합은 : {}".format(num,total))