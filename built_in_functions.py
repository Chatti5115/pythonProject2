#input() 사용자로부터 콘솔로 입력을 받는 함수
#int() 정수 자료형으로 변환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() 시퀀스 자료형에 포함되어 잇는 원소 중 최대값, 최소값
#bin(), hext() : 10진수 > 2진수 변환 / 10진수 > 16진수 변환
# user_input = input('정수를 입력하세요 : ')
# print("제곱 : ", int(user_input) ** 2)
#round() : 반올림 수행
# type() : 자료형의 종류
a = "123132"
print(int(a))
b = 12.453
print(int(b))

list = [3,3,4,6,7,87,2,23]
print(max(list))

print(bin(128))
print(hex(230))

print(int('0xe6', 16))

print(round(123.324, -1))

int = 1
str = "문자열"
list = [1,2,3]
dict = {'apple':'사과'}
print(type(str))