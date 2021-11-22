N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for x, y in lst:
    if end == 0:
        end = y
        cnt += 1
    else:
        if end <= x:
            end = y
            cnt += 1

print(cnt)