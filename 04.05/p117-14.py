'''
2023.04.05
202395005 김대영
5과목의 점수 총점과 평균을 구하는 프로그램을 작성하기
'''
#변수 선언
sub1=int(input('과목1 : '))
sub2=int(input('과목2 : '))
sub3=int(input('과목3 : '))
sub4=int(input('과목4 : '))
sub5=int(input('과목5 : '))

total=(sub1 + sub2 + sub3 + sub4 + sub5) #합계 구하기
age=(total/5) #평균 구하기

print('{}의 총점은 {}이고 평균은 {}이다.'.format('5과목 점수',total,age)) #결과 출력
