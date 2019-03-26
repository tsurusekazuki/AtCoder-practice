k = int(input())
num_list = []
for num in range(1, k+1):
    if num % 2 != 0:
        for gsu in range(1, k+1):
            if gsu % 2 == 0:
                pair = []
                pair.append(num)
                pair.append(gsu)
                num_list.append(pair)
print(len(num_list))
