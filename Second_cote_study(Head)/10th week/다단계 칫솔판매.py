'''
https://programmers.co.kr/learn/courses/30/lessons/77486

enroll = 1~10000, 민호제외 구성원 총 수, 명단
referal = enroll의 길이와 같음. enroll의 같은 idx의 부모 정보임.
        없을 수 있음. "-"로 표기됨. 조직에 참여한 순서대로 있음.
seller = 판매정보, 누가 판매했는지 . 중복 가능
amount = 몇개 판매했는지. 1이상 100이하
칫솔 하나는 100원임

2원 같이 10으로 나눴는데 0나오는거면 자기가 다 먹음. 위에 안올려줌.

부모를 계속 찾아 올라가는거면 union , find하되, 경로압축은 안해야겠는데..
쿼리가 10만개니까..일자로 된 토폴로지면 ..
10만 * 1만 = 10억 연산..

'''

def solution(enroll, referral, seller, amount):
    idx_parent = dict() 
    results =[ 0 for i in range(len(enroll))]
    # 사원들의 idx번호와 부모정보 하나에 저장.
    # 사원명이 모두 string이라 딕셔너리로 해싱해둠.
    for idx, person in enumerate(enroll):
        idx_parent[person] = [idx, referral[idx]]

    # seller를 어떻게 처리해줘야 하나.. 
    # 문제 설명대로 10만의 쿼리를 일일이 해주면 터질거같은데
    # seller를 정리해서 한번에 싹 올려주는건..? 일단 이렇게 짜자
    for i in range(len(seller)):
        idx_parent[seller[i]].append(amount[i]*100)

    #각 사원들의 판매실적 처리
    for k,v in idx_parent.items():

        #판매실적이 없을 수 있으니까.
        if len(v) <=2:
            continue

        queries = [0]*5 # 금액과 얼마나 부모를 타고올라가야하는지 count값 저장
        moneys = v[2:]
        for money in moneys:
            tmp = money
            count = 0
            while tmp != 0:
                c= tmp -int(tmp * 0.1)
                queries[count] += int(c)
                tmp //= 10

                count += 1
        person = idx_parent[k][0]

        print(k, queries)
        for now, query in enumerate(queries):
            print(person)
            if query == 0:
                break
            else:
                results[person] += query #해당 쿼리 값을 더해주고
                person_name = idx_parent[enroll[person]][1] # 부모로 포인터를 변경함
                if person_name == '-':
                    break
                else:
                    person = idx_parent[person_name][0]
        print(results)
    return results
            
"""
amount = 10 
1000
900 / 100 count = 1
90 / 10 count = 2
9 / 1 count = 3
1 / 0 count = 4
"""
        
        
        
        

def main():
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["sam", "emily", "jaimie", "edward"]
    amount = [2, 3, 5, 4]
    
    solution(enroll,referral,seller,amount)

main()