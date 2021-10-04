import math
peymaneh = int(1e9+7)
count = 0
n = int(input())

def mult(f, s, mod= peymaneh):
    return (f%mod) * (s%mod) 

# def ad(f, s, mod= peymaneh):
#     return (f%mod + s%mod - mod) % mod 

def sub(f, s, mod= peymaneh):
    return (f%mod - s%mod + mod) % mod 

# for a in range(1, int(n/3)+1, 1):
#     count = (count + sub(int(sub(n,3*a)/2), sub(max(0, int(n/2)), 2*a) +1 ) + 1)
for a in range(1, int(n/3) + 1):
    count = count + int((n - 3*a) / 2) - max(0, int(n/2) - 2*a + 1) + 1


print(count % peymaneh)
# print(type(2**2048))
# print((2**2048))
# print(type(peymaneh))
# print(peymaneh)