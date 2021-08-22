# coding=utf-8
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
dict['안녕'] = 'Hi'
# del dict['기적']
keys = dict.keys()
key_list = list(keys)
print("키 리스트 : ", key_list)
print(dict)

values = dict.values()
value_list = list(values)
print("키 값 : ", value_list)

if '노력' in dict:
    print("노력 키가 존재")

dict.clear()
print("사전 자료형의 길이 ", len(dict))
# print(dict)


# for i, k in enumerate(dict):
#     print("[인덱스 :",i, "] 한글 : ",k, "/ 영어:", dict[k])

scores ={}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한울'] = 85
print(sorted(scores)) #키로 정렬하기
print(sorted(scores, reverse=True)) #키로 내림차순 정렬
print(sorted(scores.values())) # 값을 정렬

