# len() : 문자열의 길이를 출력
# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지
# isdigit() : 특정한 문자열이 숫자로만 이루어져 잇는지
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 잇는지
# join() : 여러 개의 문자열을 구분자와 함께 합치는
# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(), lower()
# strip() 좌우로 특정한 문자열을 제거하는 함수

# eval() : 문자열 수식 계산해주는 함수
exp = "(203+705)*3-(60/3)"
print(eval(exp))

strrrr = ' Hello World '
print(strrrr.strip(' '))

strrr = "I-wanna watch a movie."
list12 = strrr.split('-')
print(list12)
print(strrr.find('watch', 5))

str ="HelloWorld"
str1 = "123"
print(str[::-1])
print(len(str))
print(str.isalpha())
print(str1.isdigit())
print(str.isalpha())

list = ['Hello','World','홍길동']
print(','.join(list))

list2 = sorted(str)
print(list2)
print(''.join(list2))
list2 = sorted(str, reverse=True)
print(''.join(list2))

