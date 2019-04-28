def gcd(a,b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

N = int(input())
A = [i for i in map(int,input().split())]
L = [0]
R = [0]
for i in range(N):
    L.append(gcd(L[-1],A[i]))
for i in range(N-1,-1,-1):
    R.append(gcd(R[-1],A[i]))
R.reverse()
g = []
for i in range(N):
    g.append(gcd(L[i],R[i+1]))
print(max(g))
