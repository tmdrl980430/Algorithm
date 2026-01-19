#알고리즘 고득점 Kit

from collections import Counter

def solution(participant, completion):
    answer = ''
    part_counter = Counter(participant)
    com_counter = Counter(completion)
    

    for key in part_counter.keys():
        if part_counter[key] != com_counter[key]:
            answer = key
            break
    
    return answer