'''
2023.05.09
202395005 김대영
1부터 100까지의 숫자 중에서 사용자로부터 입력받은 숫자의 배수 합을 구하는 프로그램을
while문과 continue문을 사용하여 구하기
#문제분석
    -변수
        정수(num) , 합계(total)
    -수식

#알고리즘
    1.변수 선언
        num을 정수로 입력 받기
        total=0

    2.논리(반복)
        i = 0
        total = 0

        while i < 100 :
            i = i + 1
            if(i % num) != 0 :
                continue
            total = total + i
        
        print(배수의 합)
'''
num=int(input("배수 숫자 입력 : "))

# 변수 초기화
i = 0
total = 0

while i < 100 :
    i = i + 1
    if(i % num) != 0 : # 배수가 아닐 때
        continue # 입력된 수의 배수가 아니면 반복문 처음으로 이동

    total = total + i # 배수만 합계에 더함

print("1부터 100까지 {}의 배수의 합은 : {}".format(num,total))