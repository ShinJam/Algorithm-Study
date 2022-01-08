from math import inf
import sys

input = sys.stdin.readline


def solution(n, s, a, b, fares):
    BOARD = [[inf]*n for _ in range(n)]

    for frm, to, fare in fares:
        BOARD[frm-1][to-1] = fare
        BOARD[to-1][frm-1] = fare

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    BOARD[i][j] = 0
                elif BOARD[i][k] + BOARD[k][j] < BOARD[i][j]:
                    BOARD[i][j] = BOARD[i][k] + BOARD[k][j]
    ret = inf
    for k in range(n):
        ret = min(ret, BOARD[s-1][k] + BOARD[k][a-1] + BOARD[k][b-1])
    return ret
