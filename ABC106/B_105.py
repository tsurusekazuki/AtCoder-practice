
n = int(input())
count = 0
for num in range(1, n+1):
    if num % 2 != 0:
        divisor_list = []
        for divisor in range(1, num+1):
            if num % divisor == 0:
                divisor_list.append(divisor)
        if len(divisor_list) == 8:
            count += 1
print(count)
