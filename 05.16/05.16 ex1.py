'''
2023.05.16
202395005 김대영
'''
f=open("C:/data/text.txt","w") # 파일 객체 ft생성(쓰기)

for i in range(1,11) : # 10번 반복
    f.write("%d번째 줄입니다.\n"%i) # ft에 i 출력

f.close() # 파일 종료
