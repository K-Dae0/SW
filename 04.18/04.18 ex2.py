'''
2023.04.18
202395005 김대영
모두 75점 이상이고 총점이 180이상이면 "최우수 학생"
총점이 160이상이면 "우수 학생"
총점이 150이상이면 "보통 학생"
두 과목의 점수가 모두 75점 이상이 아니라면 "분발합시다"출력
#문제분석
    -변수 
        숫자1(score1),숫자2(score2),합계(total)
#알고리즘
    1.변수 선언
        score1, score2에 점수 입력 받기
    2.논리(선택)
        if score1>=75 and score2>=75 :
            if total>=180 :
                print("최우수 학생")
            elif total>=160 :
                print("우수 학생")
            else :
                print("보통 학생")
        else :
            print("분발합시다")
'''
score1=int(input("첫 번째 과목의 점수 입력 : "))
score2=int(input("두 번째 과목의 점수 입력 : "))
total=score1+score2 

if score1>=75 and score2>=75 :
    if total>=180 :
        print("최우수 학생")
    elif total>=160 :
        print("우수 학생")
    else :
        print("보통 학생")
else :
    print("분발합시다")