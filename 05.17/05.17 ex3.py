'''
2023.05.17
202395005 김대영
# 문제 정의
    학생의 이름과 성적으로 'stu.txt' 파일에 저장하는 프로그램 작성    

# 문제 분석
    -변수 
        이름성적입력(score), 반복변수(i)
    -수식
        
# 알고리즘
    1. 파일 객체 생성(쓰기)
    2. 이름 성적 입력(5명-반복)
        while i <= 5 :
            score 변수에 이름 성적 입력
            파일에 쓰기

            i 1증가
'''
f=open("C:/data/stu.txt","w") # stu.txt 파일을 쓰기 모드로 설정

i=1
while i<=5 : # 5번 반복
    score=input("%d번째 학생 이름과 3과목 성적 입력(예: 홍길동 80 90 70) : "%i)

    f.write(score+"\n") # 줄 바꿈 문자를 포함하여 파일에 저장 
    i += 1 # i 1씩 증가

f.close() # 파일 종료
