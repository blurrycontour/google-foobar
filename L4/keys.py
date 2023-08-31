
from itertools import combinations

def solution(num_buns, num_required):
    if num_required == num_buns:
        return [[i] for i in range(num_buns)]
    if num_required == 1:
        return [[0] for i in range(num_buns)]

    keys = [[] for i in range(num_buns)]
    key_number = 0
    for c in combinations(keys, num_buns - num_required + 1):
        for bunny in c:
            bunny.append(key_number)
        key_number += 1

    return keys


if __name__ == "__main__":
    cases = [
        (5,3),  # [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
        (3,3),  # [[0], [1], [2]]
        (3,2),  # [[0,1], [0,2], [1,2]]
        (3,1),  # [[0], [0], [0]]
        (2,2),  # [[0], [1]]
        (2,1),  # [[0], [0]]
        (2,0),  # [[], []]
        (9,7),  # [[], []]
    ]

    for c in cases[::-1]:
        print(solution(*c))