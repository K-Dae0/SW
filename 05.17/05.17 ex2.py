'''
2023.05.17
202395005 김대영
# 문제 정의
    기존 파일의 이름과 새로운 파일의 이름을 입력받아 기존 파일의 내용을
    새로운 파일로 복사하는 프로그램을 작성

# 문제 분석
    -변수 
        원본파일(source), 복사할파일(target), 원본파일의내용(txts)
    -수식
        
# 알고리즘
    1. source에 원본파일 이름 입력
    2. target에 복사할파일 이름 입력
    3. 파일 처리
        source 파일 객체 생성
            한 줄씩 읽어 오기
            내용을 txts변수에 저장
        target 파일 객체 생성
            txts 파일 객체 생성
        파일 생성 메세지 출력
'''
source=input("source 파일 입력 : ")
target=input("target 파일 입력 : ")

with open("C:/data/LineTest.txt","r") as f : # 읽기 파일 객체

    txts=f.read() # 파일의 모든 내용을 txts에 저장

with open("C:/data/CopyLineText.txt","w") as ft : # 쓰기 파일 객체

    ft.write(txts) # txts 변수에 저장된 내용을 파일에 저장

    print(target+"파일이 생성되었습니다.") # 메세지 출력




