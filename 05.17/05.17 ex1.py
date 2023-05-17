'''
2023.05.17
202395005 김대영
'''
# for 반복문으로 파일 읽어 오기

# with를 이용하여 읽기 모드로 파일 객체 생성
with open("C:/data/LineTest.txt","r") as f :
    
    # for문에 파일 객체를 지정하면 한 줄씩 반복하며 읽기
    for line in f :

        print(line,end='') # 줄 바꿈 없이 출력

# with의 경우 f.close()를 할 필요가 없다


# readline() 메소드를 사용하여 한 줄씩 읽어 오기
print()

with open("C:/data/LineTest.txt","r") as f :

    # While문을 사용하여 무한 반복
    while True :

        line=f.readline() # 한 줄을 읽어들임
        print(line,end='') # 줄 바꿈 없이 출력

        # 읽어 들인 값이 없는 경우 반복문을 벗어남
        if line=='' : 
            break

# with의 경우 f.close()를 할 필요가 없다



# readlines() 메소드를 사용하여 한 줄씩 읽어 리스트로 반환
print()

# with를 이용하여 읽기 모드로 파일 객체 생성
with open("C:/data/LineTest.txt","r") as f :

    # 파일에 있는 모든 줄을 하나의 리스트 항목으로 만들어 반환
    textLists=f.readlines()
    
    print(type(textLists)) # textLists의 형 추가
    print(textLists) # 리스트 출력

# with의 경우 f.close()를 할 필요가 없다

# print() 함수로 파일에 출력하기
print()

# 쓰기 모드로 파일 객체 생성
f = open("C:/data/printtest.txt","w")

# 매개변수 file을 이용하여 파일객체를 지정하여 파일에 출력
print("aaaaaa",file=f)
# 파일의 다음 위치에(파일 포인터)에 출력 
print("bbbbbb",file=f) 
print("cccccc",file=f)

f.close() # 파일 종료


