'''
2023.05.24
202395005 김대영
'score1.txt' 파일에 있는 10명의 평균 자료를 읽어서 등급을 구한 후, 
화면과 'report1.txt' 파일에 출력하기
'''
score=[]
f=open("C:/data/score1.txt","r")

for i in range(10) :
    score.append(f.readline().split())

for j in range(10) :
    score[j][1]=float(score[j][1]) # 문자열을 실수로 변환

    if score[j][1] >= 90 :
        score[j].append("A")

    elif score[j][1] >= 80 :
        score[j].append("B")

    elif score[j][1] >= 70 :
        score[j].append("C")
    
    else :
        score[j].append("D")

for i in range(10) :
    print("{:<5}{:<5}".format(score[i][0],score[i][2]))

f.close()


