def sum_all(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total
print(sum_all(10))



def sum_all(n):
    return int(n*(n+1)/2)
print(sum_all(100))