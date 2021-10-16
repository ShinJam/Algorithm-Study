ret = []
def hanoi(n, frm, tmp, to):
    global ret
    if n == 0:
        return
    hanoi(n-1, frm, to, tmp)
    ret.append((frm, to))
    hanoi(n-1, tmp, frm, to)

K = int(input())
hanoi(K, 1, 2, 3)
print(len(ret))
for r in ret:
    print(*r)
