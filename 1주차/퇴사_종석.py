result = []

def back(index, rest_day, money, lst):
    global result
    

    for j in range(index, len(lst)):
        if rest_day != 0:
            rest_day -= 1
        else:
            if j + lst[j][0] -1 < len(lst):
                back(j+1, lst[j][0]-1, money + lst[j][1], lst)
    result.append(money)

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

for i, (consulting_day, money) in enumerate(lst):
    if i + consulting_day - 1 < len(lst):
        back(i+1, consulting_day-1, money, lst)
if not result:
    print(0)
else:
    print(max(result))