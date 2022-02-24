from itertools import combinations
def solution(orders, course):
    countDict = dict()
    tmp = []
    answer = []
    for c in course: # 2, 3, 4 ... 개의 course
        for i, ord in enumerate(orders): # 각 코스에 대해서
						# string으로 되어있는 ord를 list로 변환, 정렬해줍니다.
            orders[i] = sorted(list(ord)) 
						#지금 고르고자하는 코스 요리 개수대로 조합을 만들고
            combi = list(combinations(orders[i],c))

						#dictionary에 카운트를 올려줍니다.
            for com in combi:
                if com in countDict:
                    countDict[com] += 1
                else:
                    countDict[com] = 1
				#countDict에 있는 key, value를 가져와서 value순서대로 정렬합니다.
        sorted_dict= sorted(countDict.items(),key= lambda x : x[1], reverse = True)
        for i, (k, v) in enumerate(sorted_dict):
						#2개 이상 있으면 추가해야하는데
            if v >=2:
                tmp.append(k)
            # 다음에 오는 조합이 현재 조합이 불린 수보다 적어지면 그만.
            if i == len(sorted_dict)-1 or v > sorted_dict[i+1][1]:
                break
				#countDict 초기화
        countDict = dict()
    
    for t in tmp:
        ans = ''.join(t)
        answer.append(ans)
    answer.sort()
    return answer