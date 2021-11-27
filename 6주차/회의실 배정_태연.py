import sys
import heapq

N = int(input())
timetable = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(timetable, [end, start])

time_end, _ = heapq.heappop(timetable)
count = 1
for _ in range(N - 1):
    end, start = heapq.heappop(timetable)
    if time_end <= start:
        time_end = end
        count += 1
print(count)
