T = int(input())
for tc in range(T):
    N = int(input())
    lst1 = set(map(int, input().split()))
    M = int(input())
    lst2 = list(map(int, input().split()))

    for i in lst2:
        if i in lst1:
            print(1)
        else:
            print(0)