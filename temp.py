import sys

a = None
b = 0
c = a or b
d = b or a
e = a and b
f = b and a
a = [1]
print(a[-1])
print(f"{c=} {d=} {e=} {f=}")
