# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
# reverse() : 리스트의 원소를 뒤집기
# sum(리스트 자료형) : 리스트의 모든 원소의 합
# range(시작 , 끝) : 특정 범위를 지정
# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환
# all() / any() : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
# sort() : 리스트의 원소를 정렬
# count() : 특정한 원소의 개수를 추출
# del : 리스트의 특정 원소를 제거
# append() : 리스트이 가장 마지막 원소로서 원소를 삽입

# list = ['나동빈','강종구','이태일','박한울','이상욱']
# print(list.index('이태일'))
#
# list12 = [1, 2, 3]
# list12.reverse()
# print(list12)
# print(list12[::-1])
#
# list1232 = [1,2,0.23]
# print(sum(list1232))
# insert() : 리스트에 특정 원소를 삽입


my_range = range(5, 10)
list12312 = list(my_range)
print(list12312)

list24123 = [True, False, True]
print(any(list24123))

list2341234 = ['나동빈','강종구','이태일','박한울','이상욱']
result = list(enumerate(list2341234))
print(result)

for i, k in enumerate(list2341234) :
    print("인덱스 : ", i, " / 원소 : ", k)


print(list2341234.count('이태일'))

my_list = ['1234','12341','32456']
del my_list[1:3]
print(my_list)