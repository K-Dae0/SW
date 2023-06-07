'''
2023.05.30
202395005 김대영
사용자로부터 입력받은 문장을 다음과 같이 출력하기
'''
st=input("영어 문장 입력 : ")

print("입력된 문장의 길이는 :",len(st))
print("입력받은 문장의 첫 문자만 대문자 :",st.capitalize())
print("각 단어의 첫 문자를 대문자로 변환 :",st.title())
print("모든 글자를 대문자로 변환 :",st.upper())
print("모든 글자를 소문자로 변환 :",st.lower())
print("문자열에 a가 몇번 나타났는가 :",st.count('a'))
print("입력된 문자열이 모두 문자로만 구성되었는가? :",st.isalpha())
print("스페이스의 갯수 :",st.count(''))
print("스페이스를 삭제한 문자열 :",st.replace(' ',''))

