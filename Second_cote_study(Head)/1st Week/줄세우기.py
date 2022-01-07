'''
https://www.acmicpc.net/problem/10431

자기보다 큰학생이 앞에 없으면 서고 끝
한명이상 큰학생이 있으면 큰학생중 가장 앞에(가장작은학생)앞에 선다. 가장 작은 학생부터는 뒤로 한칸씩 물러선다.
'''
import sys
input  = sys.stdin.readline

P = int(input())
result = list()

for i in range(1,P+1):
    #각 테스트케이스에 대해서 변수 , input정리
    lines = []
    cnt = 0
    students = list(map(int,input().rstrip().split()))
    # 1,2,3,4 들어온거 제거
    students.remove(i)

    # 학생들 키에 대해 for문으로 하나씩 살핌
    for j, stu in enumerate(students):
        # 첫 학생 들어갈 때는 그냥 들어가면 되고
        if len(lines) == 0:
                lines.append(stu)
                continue
        # 해당 학생이 줄에서 가장 큰 키를 가지는 학생이면 그냥 맨뒤에 서면 되고
        if stu > max(lines):
            lines.append(stu)
            continue
        # 위 2개가 아니라면 자신보다 큰 학생 만나자 마자 해당 인덱스에 넣어주면 됨.
        for k, line in enumerate(lines):
            if stu < line:
                # 자신보다 큰학생부터 뒤로 한칸씩 미뤄야 하므로
                # (1,3)에 (2) 가 들어가면 (3)이 한칸 미뤄져야 하므로
                # len(1,3) = 2에서 3의 인덱스 1을 뺴주면 1칸이 나옴.
                cnt += len(lines)-k
                lines.insert(k, stu)
                break
    print(i, cnt)



            
            



