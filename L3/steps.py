def solution(n):
    # cache[left, last]
    cache = [[None for _ in range(n+1)] for _ in range(n+1)]

    def sol(left, last, cache):
        N = 0
        for m in range(last+1,left+1):
            if m < last:
                continue 
            if left-m > m:
                if left-m < 2*m + 3:
                    cache[left-m][m] = 1
                    N += 1
                else:
                    if cache[left-m][m] is None:
                        N += sol(left-m, m, cache)
                    else:
                        N += cache[left-m][m]
        cache[left][last] = N + 1   # one for case left-m <= m (count only once)
        return N + 1

    n_stairs = sol(n, 0, cache)
    # for row in cache:
    #     print(row)
    return n_stairs - 1


if __name__ == "__main__":
    cases = [3, 4, 6, 8, 200]    # 1, 1, 2, 4, 487067745

    for c in cases:
        print(solution(c))