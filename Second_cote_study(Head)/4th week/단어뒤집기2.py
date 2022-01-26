'''
https://www.acmicpc.net/problem/17413
'''
import sys
input = sys.stdin.readline

flag = False
slicing = False
line = input().strip()
s, e = 0,0
for i, c in enumerate(line):
    # <Tag> 문자 처리
    if c == "<":
        s = i
        flag = True
        continue
    # <>를 만나면 end 정하고 출력 
    elif c == ">":
        e = i+1
        flag = False
        print(line[s:e], end = '')
        continue

    #중간 단어들 거꾸로 프린트 해줘야함.
    if not flag and not slicing:
        #공백은 바로 출력하고
        if c == ' ':
            print(c, end = '')
            continue
				#처음 시작점 잡아줌
        s = i
        slicing = True

    if not flag and slicing:
        # 끝까지 도달했거나, 다음 문자가 <, 공백 이면 단어 끝난거.
        if i == len(line)-1 or line[i+1] == '<' or line[i+1] == ' ':
            e = i
            slicing = False
        # 슬라이싱이 끝났으면 바로 출력
        if slicing == False:
            while e>=s:
                print(line[e],end = '')
                e-=1