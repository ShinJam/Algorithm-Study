N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0])) 

last = times[0]
cnt = 1
for time in times[1:]:
    if time[0] < last[1]:
        continue
    last = time
    cnt += 1
print(cnt)


'''
3
1 3
8 8
4 8

일찍 시작하는 것도 정렬해야 한다.

'''
