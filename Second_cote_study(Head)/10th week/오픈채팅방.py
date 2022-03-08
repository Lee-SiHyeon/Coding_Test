'''
https://programmers.co.kr/learn/courses/30/lessons/42888

1. 채팅방 나가고 새로운 닉으로 들어옴
2. 채팅방에서 닉변

기존 출력되어있던 닉네임도 전부 변경
닉네임 중복 허용
1이상 10만 이하

Enter, Leave, Change + uid + 닉네임
'''


def solution(record):
    id_name = dict()
    logs = []
    for rec in record:
        # 출력 로그는 uid로 관리해야할거고..
        # id_name에다가 해당 id의 로그가 몇번쨰 인덱스인지도 저장해둬야겠네.
        print(rec)
        try:
            com, id, nick = rec.split()
        except:
            com, id = rec.split()
        if com == 'Enter':
            id_name[id] = [nick,[]]
            id_name[id][1].append(len(logs))
            logs.append([id, com])
        elif com == 'Leave':
            id_name[id][1].append(len(logs))
            logs.append([id, com])
        elif com == 'Change':
            id_name[id][0] = nick
    results = []
    for id, com in logs:
        if com == 'Enter':
            results.append(id_name[id][0] + "님이 들어왔습니다.")
        elif com == 'Leave':
            results.append(id_name[id][0] + '님이 나갔습니다.')
    print(results)
    return results

    
        



def main():
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"] 
    solution(record)

main()