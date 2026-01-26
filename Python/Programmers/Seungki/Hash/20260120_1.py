#해시 완주하지 못한 선수

#문제
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

from collections import Counter

def solution(participant, completion):
    answer = ''
    part_counter = Counter(participant)
    com_counter = Counter(completion)
    #key, value 형태로 만들어서 도착지에 존재하는지 확인한다.
    for key in part_counter:
        if part_counter[key] != com_counter[key]:
            answer = key
            break
    return answer
        
A = ["leo", "kiki", "eden"]
B = ["eden", "kiki"]
solution(A,B)
