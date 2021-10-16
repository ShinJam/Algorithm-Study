def hanoi(n, start, end, k):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, 6 - start - end, k + 1)
    print(start, end)
    hanoi(n - 1, 6 - start - end, end, k + 1)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3, 1)
