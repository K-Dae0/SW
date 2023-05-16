'''
2023.05.16
202395005 김대영
read(int n) , seek(0) 메소드를 사용
'''
f=open("C:/data/text.txt","r") # 파일 객체 생성(읽기)

print(f.read(10),end='') # 10개의 문자를 읽어 출력(포인터가 이동)
print(f.read(10),end='') # 다음 10개의 문자를 읽어 출력
print(f.read(10))

f.seek(0) # 포인터를 파일의 처음으로 이동

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.close() # 파일 종료