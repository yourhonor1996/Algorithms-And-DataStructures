n, energy = [int(item) for item in input().split()]
fruits1 = []
fruits2 = []
for i in range(n):
    temp1, temp2 = [int(item) for item in input().split()]
    fruits1.append(temp1)
    fruits2.append(temp2)


zipped_lists = zip(fruits1, fruits2)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
fruits1, fruits2 = [list(item) for item in tuples]

for i, enr1 in enumerate(fruits1):
    if(enr1 < fruits2[i] and energy >= enr1):
        energy += (fruits2[i] - enr1)
        # fruits.pop(key)

print(energy)
