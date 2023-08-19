def solution(s):
    right = 0
    salutes = 0
    for c in s:
        if c == '>':
            right += 1
        if c == '<':
            salutes += 2*right
    return salutes


if __name__ == "__main__":
    cases = [
        "--->-><-><-->-",   # 10
        ">----<",   # 2
        "<<>><" # 4
    ]

    for c in cases:
        print(solution(c))
