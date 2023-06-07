'''
2023.05.30
202395005 김대영
각 줄의 합을 출력하고, 모든 요소 중에서 가장 작은 값을 구하는 프로그램을 작성
'''
list1=[[11,33,22,7],[77,2,90],[3,66,44,9,8]] # 리스트 생성

minvalue=min(list1[0]) # 첫 번째 요소에서 가장 작은 값 7을 변수에 저장

for i in range(len(list1)) : # list1의 길이만큼 반복

    # sum() 함수를 사용하여 각 줄의 합 출력
    print(i + 1,"번째 줄의 합 : ",sum(list1[i]))

    if minvalue > min(list1[i]) : # 각 줄의 가장 작은 값 비교
        minvalue = min(list1[i])

print("리스트에서 가장 작은 값 :", minvalue)

