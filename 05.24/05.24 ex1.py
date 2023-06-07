'''
2023.05.24
202395005 김대영
1~100 사이의 난수를 발생시켜 'num.txt' 파일을 생성하고, 생성된 'num.txt' 파일을
읽어 각 학생의 평균을 'avg.txt' 파일에 출력하는 프로그램을 작성        
'''
import random
with open("C:/data/num.txt","w") as f :
    for i in range(5) :
        for j in range(5) :
            f.write(str(random.randint(1,100)))
            f.write(' ')
        f.write('\n')


with open("C:/data/num.txt","r") as f1 :
    with open("C:/data/avg.txt","w") as f2 :
        j=0


        while True :
            j+=1
            score=f1.readline() # num.txt 한 줄 읽어 오기
            if score=='' :
                break

            scorelist=score.split()
            sum=0

            for i in range(5) :
                sum=sum+int(scorelist[i])

            print("%d번째 학생의 평균 : "%j,sum/5,file=f2)