N = int(input())

A = bin(N)
cnt = 0
for a in A:
    if a == '1':
        cnt +=1

print(cnt)