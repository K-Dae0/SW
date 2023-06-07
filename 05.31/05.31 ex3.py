'''
2023.05.31
202395005 김대영
# 문제 정의
    두 개의 튜플을 생성하고, 튜플로부터 하나의 리스트를 생성하는 프로그램을 작성

# 문제 분석
    -변수
        과일 튜플(fruit), 가격 튜플(price)
    -수식

# 알고리즘
    1.튜플 생성
    2.빈 리스트 생성
    2.반복(두개의 튜플을 하나의 리스트로 합치기)
        for i in range(len(fruit))
        fruit[i]->fp_list 추가
        price[i]->fp_list 추가
'''
fruit=('사과','배','파인애플','포도') # 튜플 생성
price=(5000,7000,4500,6000)

fp_list=[] # 빈 리스트 생성

for i in range(len(fruit)) : # 튜플의 길이만큼 반복
    fp_list.append(fruit[i]) # fruit의 i번째 값을 리스트에 추가
    fp_list.append(price[i]) # price의 i번째 값을 리스트에 추가

print("과일 튜플 :",fruit)
print("가격 튜플 :",price)
print("튜플로부터 생성된 과일+가격 리스트 :", fp_list)