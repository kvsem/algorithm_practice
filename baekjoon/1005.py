# TODO K : 위상정렬

t = int(input())

for i in range(t):
    cost = 0
    order_info = dict()
    cost_info = dict()
    max_num, case_count = map(int, input().split())
    cost_list = list(map(int, input().split()))

    for j in range(case_count):
        start, dest = map(int, input().split())

        if cost_info.get(dest):
            if cost_info.get(dest) < cost_list[start - 1]:
                order_info[dest] = start
                cost_info[dest] = cost_list[start - 1]
            else:
                cost_info[dest] = cost_info.get(dest)

        else:
            order_info[dest] = start
            cost_info[dest] = cost_list[start - 1]

    final = int(input())
    cost += cost_list[final - 1]

    _next = final
    while _next:
        cost += cost_info.get(_next, 0)
        _next = order_info.get(_next)

    print(cost)
