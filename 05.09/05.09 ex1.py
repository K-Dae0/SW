'''
2023.05.09
202395005 김대영
두 개의 숫자를 입력받아 두 수 사이의 모든 정수값을 더하여 출력하는 프로그램 구하기
#문제분석
    -변수
        정수1(num1) , 정수2(num2) , 합계(sum) , 임시변수(temp)
    -수식
        
#알고리즘
    1.변수 선언
        num1 , num2를 정수로 입력 받기
        sum=0 , temp=0

    2.논리(선택,반복)
        if num1 > num2 :
            
            temp=num1
            num1=num2
            num2=temp
        
        print(end=' ')
        sum=0

        i=num1
        while i <= num2 :

            sum = sum + i
            i = i + 1

        print(sum)    
'''
num1=int(input("첫 번째 숫자 입력 : "))
num2=int(input("두 번째 숫자 입력 : "))

if num1 > num2 : #num1이 num2 보다 크다면 두 수를 바꿔준다

    temp=num1 #두 수 교환
    num1=num2
    num2=temp

print(num1,"부터",num2,"까지의 합은 :",end=' ') #end를 사용하여 인쇄 후에 줄을 바꾸지 않는다
sum=0

i=num1 #while문을 사용하기 위해 num1을 변수 i로 지정
while i <= num2 : # i가 num2보다 작거나 같을 때까지 반복
    
    sum=sum+i
    i=i+1

print(sum) #결과 출력