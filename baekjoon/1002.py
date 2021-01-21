n = input()

for i in range(int(n)):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    distance = pow(x1 - x2, 2) + pow(y1 - y2, 2)
    r_sum_pow = pow(r1 + r2, 2)
    r_sub_pow = pow(r1 - r2, 2)

    if distance == r_sum_pow or distance == r_sub_pow:
        print(1)
    elif distance > r_sum_pow or distance < r_sub_pow:
        print(0)
    else:
        print(2)