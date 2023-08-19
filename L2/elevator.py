def solution(l):
    # l = sorted(l, key=lambda x: int(x.split('.')[2]) if len(x.split('.')) > 2 else 0)
    # l = sorted(l, key=lambda x: int(x.split('.')[1]) if len(x.split('.')) > 1 else 0)
    # l = sorted(l, key=lambda x: x.split('.')[0])
    key=lambda x: sum([int(j)*10000**int(2-i) for i,j in enumerate(x.split('.'))]) + len(x.split('.'))*0.1
    l = sorted(l,  key=key)
    return l


if __name__ == "__main__":
    cases = [
        ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
        ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
    ]

    for c in cases:
        print(solution(c))
