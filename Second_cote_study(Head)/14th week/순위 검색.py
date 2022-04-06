'''
https://programmers.co.kr/learn/courses/30/lessons/72412


흠...
개발언어 3종
지원직군 2종
경력 2종
소울푸드 2종

[조건]을 만족하는 사람 중 코테 X점 이상 받은 사람은 몇명 ?

쿼리에 조건들 + ['-']이 추가될 수 있음
'-'이면 조건 상관안하겠다는 의미

'-'을 추가해서..
4종 , 3종, 3종, 3종 = 4*3*3*3 = 12*9 = 108
아니 이게 왜 2레벨이야 ?

info 1 ~ 5만
query 1~ 10만개
'''

def solution(info, query):
    languages = ['cpp','java', 'python', '-']
    positions = ['backend', 'frontend', '-']
    careers = ['junior', 'senior', '-']
    foods = ['chicken', 'pizza', '-']

    info_comb = {}
    for l in languages:
        for p in positions:
            for c in careers:
                for f in foods:
                    #l,p,c,f
                    info_comb[' '.join([l,p,c,f])] = []
    
    for inf in info:
        l,p,c,f, score = inf.split()
        score = int(score)
        # cpp 이라면 cpp에도 들어갈 수 있고 '-'에도 들어갈 수 있음.
        for la in [l, '-']:
            for po in [p, '-']:
                for ca in [c, '-']:
                    for fo in [f, '-']:
                        info_comb[' '.join([la,po,ca,fo])].append(score)
    
    for key in info_comb:
        info_comb[key].sort()
    answers = []
    for q in query:
        l = q.split()
        qu = []
        for word in l:
            if word != 'and':
                qu.append(word)
        score = int(qu[-1])
        qu.pop()
        key = ' '.join(qu)

        left, right = 0, len(info_comb[key])-1
        mid = left+ (right-left)//2
        idx = right+1
        while left <= right:
            # mid를 콕 집었을 때 점수가 타겟 점수 score보다 같거나 커야함.
            if info_comb[key][mid] >= score:
                idx = min(idx, mid)
                right = mid-1
            else:
                left = mid+1
            mid = left + (right-left)//2
        
        answer = len(info_comb[key]) - idx
        answers.append(answer)
    return answers
    

    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))