'''
2023.05.31
202395005 김대영
# 문제 정의
    다음과 같은 튜플을 생성하고, 각 요소가 튜플에 몇번 나타났는지를
    출력하는 프로그램을 작성

# 문제 분석
    -변수
        정수 튜플(num) 
    -수식

# 알고리즘
    1.튜플 생성
    2.빈 리스트 생성
    3.반복(for)
        for i in range(len(num))
        리스트에 없는 경우 출력
        리스트에 추가
        개수 출력
'''
num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0) # 튜플 생성
print("생성된 튜플 :", num)

num_list=[] # 중복 출력 하지 않기 위해 빈 리스트 생성

for i in range(len(num)) : # 튜플의 길이만큼 반복

    if num[i] not in num_list : # 리스트에 없는 경우 출력

        num_list.append(num[i]) # 리스트에 추가
        print(num[i],"개수 :",num.count(num[i])) # 개수 출력

