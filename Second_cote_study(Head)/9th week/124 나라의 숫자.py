def solution(n):
    answer = ''
    while n != 0:
        m = n%3
        if m == 0:
            n//=3
            n -= 1
            m = 4
        else:
            n //= 3
        answer = str(m)+answer
    return answer