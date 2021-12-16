


"""
들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일하다. 이는 루트를 제외한 모든 노드에 성립해야 한다.
"""


cnt = 1
lst2 = []
while True:
    lst = list(map(int, input().split()))
    if not lst:
        continue

    elif lst[-2] == 0 and lst[-1] == 0:
        lst2.append(lst)
        tree_cnt = {}
        node = {}

        for i in range(len(lst2)):
            for j in range(0, len(lst2[i]), 2):
                if lst2[i][j] == 0 and lst2[i][j+1] == 0:
                    break
                tree_cnt[lst2[i][j]] = 0
                tree_cnt[lst2[i][j+1]] = 0

        for i in range(len(lst2)):
            for j in range(0, len(lst2[i]), 2):
                if lst2[i][j] == 0 and lst2[i][j+1] == 0:
                    break

                if lst2[i][j] not in node:
                    node[lst2[i][j]] = [lst2[i][j+1]]
                else:
                    node[lst2[i][j]].append(lst2[i][j+1])
                tree_cnt[lst2[i][j+1]] += 1
        print(tree_cnt)
        zero_count = 0
        zero_check = []
        flag = 0
        count2 = 0
        for key, value in tree_cnt.items():
            if value == 0:
                zero_check.append(key)
            elif value > 1:
                flag += 1

        if len(lst) == 2 and lst[0] == 0 and lst[1] == 0:
            print("Case {} is a tree.".format(cnt))

        elif len(zero_check) > 1 or flag == 1:
            print("Case {} is not a tree.".format(cnt))
        else:
            for key, value in node.items():

                if key == zero_check[0]:
                    continue
                else:
                    for value2 in value:
                        if value2 in node[zero_check[0]]:
                            count2 += 1

            if count2 == 0:

                print("Case {} is a tree.".format(cnt))
            else:
                print("Case {} is not a tree.".format(cnt))

        cnt += 1
        lst2 = []

    elif lst[-2] == -1 and lst[-1] == -1:
        break
    else:
        lst2.append(lst)

