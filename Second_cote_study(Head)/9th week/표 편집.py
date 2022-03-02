'''
https://programmers.co.kr/learn/courses/30/lessons/81303
n = 행 개수
k = 처음 행 위치
cmd = 명령어
'''
def solution(n, k, cmd):
    table = []
    for i in range(n):
				# 첫행의 이전 idx는 자기자신,
				# 마지막 행의 다음 idx는 자기 자신을 가리키게끔 설정
        table.append([max(0,i-1),'O',min(i+1,n-1)])
    now = k
    removed = []
    for c in cmd:
        c= c.split()
        if c[0] =='D': # c[1]만큼 아래로 이동
            for i in range(int(c[1])):
                now = table[now][2]

        elif c[0] == 'U': # c[1]만큼 위로 이동
            for i in range(int(c[1])):
                now = table[now][0]
        elif c[0] == 'C': 
            # 현재 행 삭제, 마지막열을 삭제하는거면 이전행 선택,
            # 아니라면 다음행 선택.
            table[now][1] = 'X'
            prev = table[now][0]
            next = table[now][2]
						# 복구 매커니즘에 사용할 스택에 기존 정보 저장
            removed.append([now,prev,next])
            # 마지막 행을 지우는 경우
            if now == table[now][2]:
                table[prev][2] = prev
                now = prev
						# 첫번째 행을 지우는 경우
            elif now == table[now][0]:
                table[next][0] = next
                now = next
            else:
                table[prev][2] = next
                table[next][0] = prev
                now = next
            
        elif c[0] == 'Z':
            if removed:
                rem, prev, next = removed.pop()
                table[rem][1] = 'O'
                table[rem][0] = prev
                table[rem][2] = next
                
								#첫번쨰 행이 복구되는 경우엔 prev조작 안함
                if prev != rem:
                    table[prev][2] = rem
                #마지막 행이 복구되는 경우엔 next조작 안함
                if next != rem:
                    table[next][0] = rem
    answer = ''
    
    for i in range(n):
        answer += table[i][1]
    return answer