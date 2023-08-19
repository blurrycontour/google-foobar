def solutionR(n):
    n = int(n)
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + solutionR(n/2)
    else:
        return 1 + min(solutionR(n-1),solutionR(n+1))

def solution(n):
    n = int(n)
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n % 4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
        steps += 1
    return steps

if __name__ == "__main__":
    cases = ['15', '4', '28'] # 5, 2

    for c in cases:
        print(solution(c))