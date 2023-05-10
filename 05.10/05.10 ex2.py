'''
2023.05.09
202395005 김대영
사용자로부터 정수를 반복적으로 입력받아 정수의 합이 1000 이상이 되었을 때의 결과값과
평균을 구하여 출력하는 프로그램 구하기
#문제분석
    -변수
        정수(num) , 합계(sum) , 입력횟수(cnt) , 평균(avg) 
    -수식

#알고리즘
    1.변수 초기화
        num을 정수로 입력 받기
        sum , cnt , avg = 0        

    2.논리(반복문안에 선택포함)
        sum = 0
        cnt = 0
        avg = 0

        while True :
            num = int(input(숫자입력))
            sum = sum + num
            cnt = cnt + 1
            if sum >= 1000 :
                break
        
        print(1000을 넘은 수)
        print(평균)
'''

sum = 0
cnt = 0
avg = 0

while True : 
    num=int(input("숫자를 입력 : "))
    sum=sum+num
    cnt=cnt+1
    if sum >= 1000 :
        break

avg=sum/cnt
print("1000을 넘은 수 : %d"%sum,end='')
print(",평균은 : %.2f"%avg)