import sys

N = int(sys.stdin.readline())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def TSP(dists):
    N = len(dists)
    visited_all = (1 << N) - 1
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == visited_all:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
                cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)


print(TSP(roads))