'''
2023.05.16
202395005 김대영
'''
f=open("C:/data/text.txt","r") # 파일 객체 생성(읽기)

txts=f.read() # 파일의 전체 내용을 txts에 하나의 문자열로 저장

print(txts) # 읽은 내용을 출력

f.close # 파일 종료

