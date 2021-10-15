import sys

n = int(sys.stdin.readline().rstrip())

def hanoi(n, start, fin, other):

    if n < 2:       
        print(start, fin)
        return

    hanoi(n-1, start, other, fin)
    print(start, fin)
    hanoi(n-1, other, fin, start)

print((2**n)-1)     

hanoi(n, 1, 3, 2)
