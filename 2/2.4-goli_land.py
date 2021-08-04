n, days = list(int(item) for item in input().split())
tolerances = list(int(item) for item in input().split())
temps = []
for i in range(days):
    temps.append(int(input()))

sad_people = []

for i, temperature in enumerate(temps):
    count = 0
    for j, tolerance in enumerate(tolerances) :
        if (tolerance < temperature):
            count += 1
    sad_people.append(count)
for num in sad_people:
    print(num)    