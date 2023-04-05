'''
2023.04.05
202395005 김대영
본봉과 수당을 입력 받아서 이번달 월급 수령액을 구하는 프로그램 구하기
'''
#변수 선언
sal=int(input('본봉 : '))
all=int(input('수당 : '))

total = sal + all #총액 구하기
tax = total * 20/100 #세금 구하기
amo = total - tax #수령액 구하기

print('이번달 월급 수령액은 {}만 이다.'.format(amo)) #결과 출력

