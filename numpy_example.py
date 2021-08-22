import numpy as np
# array = np.random.randint(1, 10, size=4).reshape(2, 2)
# print(array)
#
# result_array = array*10
# print(result_array)

# array12 = np.arange(4).reshape(2,2)
# print(array12)
# array14 = np.arange(2)
# print(array14)
# array13 = array12 + array14
# print(array13)

# array1 = np.arange(0, 8).reshape(2, 4)
# array2 = np.arange(0, 8).reshape(2, 4)
# array3 = np.concatenate([array1, array2], axis=0)
# array4 = np.arange(0, 4).reshape(4, 1)
# print(array3 + array4)

#
# array1= np.arange(16).reshape(4,4)
# print(array1)
# array2 = array1<10
# print(array2)
#
# array1[array2] = 100
# print(array1)

array = np.arange(16).reshape(4,4)
print("최대값 : ", np.max(array))
print("최소값 : ", np.min(array))
print("합계 : ", np.sum(array, axis=0))
print("평균 : ", np.mean(array))

print(array)
