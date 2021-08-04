Set = [1, 2, 3]
n = 3
# 1<<n = 2**n (in PYTHON)
for mask in range(1<<n):
    for i in range(n):
        value = 1<<i
        if mask & value:
            print(Set[i], end=' ')
    print()


# print(1<<3)