def solution1(start, length):
    ids = []
    for i, n_workers in enumerate(range(length, 0, -1)):
        ids.extend([start+j for j in range(n_workers)])
        start += length
    checksum = reduce(lambda x,y: x^y, ids)
    return checksum

def solution2(start, length):
    _checksums = [[]]*length
    for i, n_workers in enumerate(range(length, 0, -1)):
        _checksums[i] = start
        for j in range(1,n_workers):
            _checksums[i] ^= start+j
        start += length
    checksum = reduce(lambda x,y: x^y, _checksums)
    return checksum

def solution3(start, length):
    checksum = None
    for i, n_workers in enumerate(range(length, 0, -1)):
        _checksum = start
        for j in range(1,n_workers):
            _checksum ^= start+j
        if i == 0:
            checksum = _checksum
        else:
            checksum ^= _checksum
        start += length
    return checksum

def solution(start, length):
    def onexor(x):
        if x % 4 == 0:
            return 0
        if x % 4 == 1:
            return x-1
        if x % 4 == 2:
            return 1
        if x % 4 == 3:
            return x
    
    checksum = None
    for i in range(length):
        row_checksum = onexor(start)^onexor(start+length-i)
        if i == 0:
            checksum = row_checksum
        else:
            checksum ^= row_checksum
        start += length
    return checksum


if __name__ == "__main__":
    cases = [(17,4), (0,3), (0,10000)]    # 14, 2, 82460672

    for c in cases:
        print(solution(*c), solution3(*c), solution2(*c), solution1(*c))
        # solution - best
        # solution3 - ok
        # solution2 - bad
        # solution1 - worst