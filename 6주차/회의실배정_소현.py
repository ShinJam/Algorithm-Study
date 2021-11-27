#예전풀이
import sys

n = int(sys.stdin.readline().rstrip())

time = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

time.sort()
time.sort(key=lambda x:x[1])

room = 1
end_time = time[0][1]

#range(1,n)
for i in range(1, n):
    if time[i][0] >= end_time:
        room += 1
        end_time = time[i][1]
print(room)
