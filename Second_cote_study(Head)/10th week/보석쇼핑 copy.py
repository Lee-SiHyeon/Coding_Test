'''
https://programmers.co.kr/learn/courses/30/lessons/67258
'''

def solution(gems):
    kind_gems = len(set(gems))
    gems_dict = {}
    SIZE = len(gems)
    lp, rp = 0, 0
    min_length = 100_000
    answer = []
    while lp <= rp and rp <SIZE:
        
        if len(gems_dict) < kind_gems:
            if gems[rp] in gems_dict:
                gems_dict[gems[rp]] += 1
            else:
                gems_dict[gems[rp]] = 1
            rp += 1
            
        while len(gems_dict) == kind_gems:
            if rp-lp+1 < min_length:
                min_length = rp-lp+1
                answer = [lp+1, rp]
            if gems[lp] in gems_dict:
                gems_dict[gems[lp]] -= 1
                if gems_dict[gems[lp]] == 0:
                    gems_dict.pop(gems[lp])
            lp += 1

    return answer   
        




def main():
    gems = ["A", "A", "B"]
    print(solution(gems))

main()