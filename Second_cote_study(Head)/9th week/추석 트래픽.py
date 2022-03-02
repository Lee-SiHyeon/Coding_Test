MAX_END = 86400999 # 23:59:59.999 0.1s
def solution(lines):
    line_lists = []
    for line in lines:
        date, time, t =line.split()
				#문제의 최소단위인 ms로 변환해서 풀이.
        ms = 0
        ms += int(time[:2])*60 * 60 * 1000 # 시간 * 분(60) * 초(60) * ms(1000)
        ms += int(time[3:5]) * 60 * 1000
        ms += int(time[6:8]) * 1000
        ms += int(time[9:])
        t = t[:-1]
        t = float(t)*1000
        t = int(t)
				
				# start지점을 1초만큼 왼쪽으로 보내줍니다.
				# 다만, 이때도 시작시간이 포함되므로 -1000이 아닌 -1000+1을 계산합니다.
        start = max(0,ms-t+1-999)
        end = ms
				# end를 기준으로 하는 풀이도 가능합니다.
				# start = ms-t+1
        # end = min(MAX_END, ms+999)

        line_lists.append((start,False))
        line_lists.append((end,True))
    
		#이젠 괄호문제와 비슷하게 풀어주면됩니다.
    line_lists.sort()
    max_count = 0
    count = 0
    for i,line_list in enumerate(line_lists):
				# start라면 1을 더하고, end면 1을 감소시키면서 count의 최댓값을 갱신합니다.
        if line_list[1] == False:
            count += 1
        else:
            count -= 1
        max_count = max(max_count, count)
    return max_count