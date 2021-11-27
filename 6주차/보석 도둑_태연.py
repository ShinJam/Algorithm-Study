import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewelrys = []
bags = []

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(jewelrys, temp)

for _ in range(K):
    temp = int(sys.stdin.readline())
    heapq.heappush(bags, temp)

answer = 0
candi = []
while bags:
    bag = heapq.heappop(bags)
    while jewelrys and jewelrys[0][0] <= bag:
        weight, value = heapq.heappop(jewelrys)
        heapq.heappush(candi, -value)

    if candi:
        answer += (-heapq.heappop(candi))
    else:
        if len(jewelrys) == 0:
            break

print(answer)
