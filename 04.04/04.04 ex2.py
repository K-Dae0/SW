'''
2023.04.04
202395005 김대영
표준 출력 포맷 연습
'''
print('이름은 {}이고 나이는 {}세 입니다'.format('김대영',20))

print('이름 {name}, 나이 {age}, 주소 {add}'.format(add='Busan',age=20,name='김대영'))

print('The lucky number is ({:14})'.format(7777)) #기본 숫자는 오른쪽 정렬

print('The lucky number is ({:<14})'.format(7777)) #'<'를 사용한 숫자 왼쪽 정렬
