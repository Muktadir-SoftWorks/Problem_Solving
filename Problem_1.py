#Triplet Sum

N = int(input())  # array size

i = (input())  # takes input all at once
values = list(map(int, i.split()))  # mapping and splitting then storing
values.sort()

P = int(input())  # target value

count = 0  # to count progress
data = P - values[0]

for x in range(0, N):
    for y in range(x + 1, N):
        for z in range(y + 1, N):
            if values[x] + values[y] + values[z] == P:
                count += 1
                print(f"{values[x]} {values[y]} {values[z]}")
                break

    if count == 1:
        break