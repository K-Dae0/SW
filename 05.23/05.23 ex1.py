'''
2023.05.17
202395005 김대영
# 문제 정의
    'stu.txt'파일을 읽어들여 각 학생의 평균 성적을
    계산하여 출력하는 프로그램을 작성

# 문제 분석
    -변수 
        한줄씩읽어서저장(score), 리스트자료로변환(scorelist), 
        이름(name), 합계(sum)
    -수식
        
# 알고리즘
    1. 파일 객체 생성(읽기)
    2. 
'''
f=open("C:/data/stu.txt","r") # 읽기 모드

lines=f.readlines()

for score in lines :

    # split() 메소드 이용(스페이스 기준 리스트 객체로 반환)
    scorelist=score.split()
    name=scorelist[0] # 0번째 항목은 이름으로 설정

    sum=0

    for i in range(1,4) : # 리스트의 성적부분을 반복
    
        sum=sum+int(scorelist[i])
    
    print(name+"의 평균 성적은 :%.1f"%(sum/3))

f.close() # 파일 종료

