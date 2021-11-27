import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []

for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])  # Max heap
        heapq.heappop(jewelryList)

    if temp:
        result += heapq.heappop(temp)
    elif not jewelryList:
        break

print(-result)

# https://kyoung-jnn.tistory.com/entry/백준1202번파이썬Python-보석-도둑-우선순위-큐

''' 시초
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x:-x[1])
bags.sort()

ret = 0
for m, v in jewels: # 무게, 가치
    for i in range(len(bags)):
        if bags[i] and m <= bags[i]:
            bags[i] = False
            ret += v
print(ret)
'''
