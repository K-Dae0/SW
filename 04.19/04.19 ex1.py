'''
2023.04.19
202395005 김대영
성별,키,몸무게를 입력받아 '표준체중','과체중','비만 체중'을 출력하고
성별이 맞지 않는 경우 '성별 입력이 잘못 되었습니다.'를 출력하는 프로그램을 구하기
#문제분석
    -변수 
        성별(sex),키(height),몸무게(weight),평균BMI(avg)
    -수식
        sex==M,m
            avg=height*height*22
        sex==F,f
            avg=height*height*21
#알고리즘
    1.변수 선언
        sex를 입력 받기
        height, weight를 실수로 입력 받기
    2.논리(내포된 선택)
        if 성별이 남자일 때 :
            avg 계산
            if weight / avg * 100 >= 120 :
                "비만 체중"
            elif weight / avg * 100 >= 119 :
                "과체중
            else :
                "표준체중"

        elif 성별이 여자일 때 :
            avg 계산
            if weight / avg * 100 >= 120 :
                "비만 체중"
            elif weight / avg * 100 >= 119 :
                "과체중
            else :
                "표준체중"

        else
            "성별을 잘못 입력" 
'''
sex=input("성별 입력('M or m' 또는 'F or f') : ") # 성별 입력 받기
height=float(input("키 입력(cm) : ")) / 100 # 키를 실수로 입력 받은 후 m단위로 변환(나누기 100)
weight=float(input("몸무게 입력(kg) : ")) # 몸무게를 실수로 입력 받기

if sex=='M' or sex=='m' : # 성별이 남자일 때
    avg=height*height*22    
    if 110 <= weight/avg*100 <= 119 :
        print("과체중")
    elif weight/avg*100 >= 120 :
        print("비만 체중")
    else :
        print("표준체중")

elif sex=='F' or sex=='f' : # 성별이 여자일 때
    avg=height*height*21
    if 110 <= weight/avg*100 <= 119 :
        print("과체중")
    elif weight/avg*100 >= 120 :
        print("비만 체중")
    else :
        print("표준체중")

else : # 성별이 맞지 않을 때
    print("성별 입력이 잘못 되었습니다.")