hash_table = list([i for i in range(10)])
print(hash_table)

def hash_func(key):
    return key % 5
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

#ord() : 문자의 ASCII(아스키) 코드 리턴

print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), ord(data1[0])%5)
print(ord(data1[0]), hash_func(ord(data1[0])))


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy','0104234')
storage_data('Dave','1235415')
storage_data('Trump','2345')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))

print(hash("Dave"))
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8
def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave','2435234')
save_data('Andy','456874567')
print(read_data('Dave'))
print(hash_table)




