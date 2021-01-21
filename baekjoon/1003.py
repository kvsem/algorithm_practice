def count_fibonacci(_n):
    _zero_count = [1, 0]
    _one_count = [0, 1]

    if _n < 2:
        return None, None

    for i in range(2, _n + 1):
        _zero_count.append(_zero_count[i - 1] + _zero_count[i - 2])
        _one_count.append(_one_count[i - 1] + _one_count[i - 2])

    return _zero_count, _one_count


n = int(input())
zero_count, one_count = count_fibonacci(40)

for _ in range(n):
    m = int(input())
    print(f"{zero_count[m]} {one_count[m]}")
