n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
num = 0
for v, c in zip(V, C):
    if v > c:
        num += v-c
print(num)
