'''> numberOfTriangles(n)
n : the sum of all three edges
-------------------------------------------------
Count the number of triples with sum equal to 'n'
that are triangular
-------------------------------------------------
1. bound := [([n/2]+1)/2]
2. answer := (bound) * (bound + 1) - [n/2] * bound +  [n/3] - bound
3. k := [[n/3] / 2]
4. answer := answer + (n+1)*k - 3*k*(k+1)
5. if [n / 3] mod 2 is 1:
6.    answer := answer + [(n - 3*(2*k+1)) / 2]
7. return answer '''

peymaneh = int(1e9+7)
n = int(input())

from math import floor as fl
bound = fl((fl(n/2) + 1) / 2)
answer = bound * (bound + 1) - fl(n/2)*bound + fl(n/3) - bound
k = fl(fl(n/3) / 2)
answer = answer + (n+1)*k - 3*k*(k+1)
if((fl(n/3) % 2) == 1):
    answer = answer + fl((n - 3*(2*k + 1)) / 2)
    
print(answer % peymaneh)

