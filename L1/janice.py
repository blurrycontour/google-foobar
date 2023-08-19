def solution(x):
    n = 'abcdefghijklmnopqrstuvwxyz'
    r = n[::-1]
    trans = {k:v for k,v in zip(n,r)}
    y = ''
    for l in x:
        y += trans.get(l,l)
    return y

if __name__ == "__main__":
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))