n = int(input())
blue = []
red = []
score_list = []
for i in range(n):
    blue.append(input())
m = int(input())
for j in range(m):
    red.append(input())
for value in blue:
    score = 0
    for s in blue:
        if value == s:
            score += 1
    for t in red:
        if value == t:
            score -= 1
    if score not in score_list:
        score_list.append(score)
if max(score_list) < 0:
    print(0)
else:
    print(max(score_list))
