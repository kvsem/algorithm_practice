def check_is_inside(x, y, _circle_x, _circle_y, _circle_r):
    # 점이 원 안에 존재하는지 판단
    return pow((x - _circle_x), 2) + pow((y - _circle_y), 2) < pow(_circle_r, 2)


t = int(input())

for i in range(t):
    count = 0
    start_x, start_y, dest_x, dest_y = map(int, input().split())

    circle_count = int(input())
    for j in range(circle_count):
        circle_x, circle_y, circle_r = map(int, input().split())
        is_start_inside = check_is_inside(start_x, start_y, circle_x, circle_y, circle_r)
        is_dest_inside = check_is_inside(dest_x, dest_y, circle_x, circle_y, circle_r)

        if (is_start_inside and not is_dest_inside) or (not is_start_inside and is_dest_inside):
            # 시작점이 원 안에 있으며 도착점이 원 밖에 있거나 시작점이 원 밖에 있으며 도착점이 원 안에 있는 경우 - 행성계 진입/이탈
            count += 1

    print(count)
