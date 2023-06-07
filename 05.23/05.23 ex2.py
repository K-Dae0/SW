'''
2023.05.17
202395005 김대영
# 문제 정의
    사용자로부터 여러 문장을 입력받아 'out.txt'파일에 저장하는 프로그램 작성
# 문제 분석
    -변수 
        입력값저장(enter), 키보드입력값저장(text)
    -수식
        
# 알고리즘
    1. 변수 초기화
        enter=[]
    2. 파일 객체 생성(쓰기)
    3.파일처리
        1.(반복) while True :
            2.텍스트라는 변수에 문장을 입력
            (선택) if text=='':
                break
            text를 enter에 추가

        3.파일에 결과 출력
        4.파일 받기
'''
enter=[]

f=open("C:/data/out.txt","w") # 쓰기 모드로 파일 객체 생성

while True : # 무한 반복
    text=input("저장할 문장입력 : ")
    if text=='' : # 입력된 문장이 없는 경우 break로 빠져나옴
        break
    enter.append(text+'\n') # 줄 바꿈 문자와 함께 리스트에 추가

print("입력될 리스트 : ",enter)

f.writelines(enter) # 리스트를 파일에 출력

f.close # 파일 종료

print("out.txt 파일이 생성되었습니다")