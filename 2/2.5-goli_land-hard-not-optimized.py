# this solution is not acceptible and must be optimized

n, days = list(int(item) for item in input().split())
tolerances = list(int(item) for item in input().split())
temps = []
for i in range(days):
    temps.append(int(input()))
tolerances.sort(reverse=True)
sad_people = []

for temperature in enumerate(temps):
    count = 0
    for tolerance in enumerate(tolerances) :
        if(tolerance < temperature):
            count += 1
        else:
            break
    sad_people.append(count)
for num in sad_people:
    print(num)    