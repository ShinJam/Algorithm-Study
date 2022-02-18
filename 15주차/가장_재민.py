import sys
input = sys.stdin.readline
T=int(input())

for _ in range(T):
    N=int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        p,c=map(int, input().split())
        parent[c]=p
 
    a,b = map(int,input().split())
    a_parent=[a]
    b_parent=[b]

    while parent[a]:
        a_parent.append(parent[a])
        a=parent[a]
 
    while parent[b]:
        b_parent.append(parent[b])
        b=parent[b]
 
 
 
    a_level=len(a_parent)-1
    b_level=len(b_parent)-1
    while a_parent[a_level]==b_parent[b_level]:
        a_level-=1
        b_level-=1
 
    print(a_parent[a_level+1])
