import heapq

N, K = map(int, input().split())
jewels = [list(map(int , input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
bags.sort(reverse=True)
cnt = 0
jewels.sort(key=lambda x: -x[0])
heap = []

# 가방은 무게순으로 정렬
# 보석도 무게순으로 정렬
# deque 안쓰려고 역순으로 정렬해놈

while bags and jewels:

    target = bags.pop() # 가장 작은 무게의 가방을 뽑는다
    while jewels and jewels[-1][0] <= target: # 뽑은 가방에 들어 갈 수 있는 모든 보석들을 heap 에 넣어준다
        jewel = jewels.pop()
        heapq.heappush(heap, [-jewel[1], jewel[0]])

    if heap: # heap 에 들어간 것중 가장 비싼 보석을 뽑는다.
        cnt += abs(heapq.heappop(heap)[0])

print(cnt)
