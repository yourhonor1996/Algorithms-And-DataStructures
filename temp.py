import sys

a = None
b = 0
c = a or b
d = b or a
e = a and b
f = b and a

print(f"{c=} {d=} {e=} {f=}")
