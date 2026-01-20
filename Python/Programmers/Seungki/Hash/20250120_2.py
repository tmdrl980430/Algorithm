# 폰켓몬

def solution(nums):
    answer = 0
    length = len(nums) // 2
    #가져갈 수 있는 폰켓몬 수를 정하기 위해서 정렬
    nums.sort()
    last = 0
    
    for value in nums :
        #가져갈 수 있는 폰켓몬 수를 찾기 위해서 찾았을 경우에만 넘어가고
        #같은 경우에는 
        if(value != last and answer < length):
            answer +=1
            last = value
            
    return answer

A = [3,1,2,3]
#A = [3,3,3,2,2,4]	
#A = [3,3,3,2,2,2]
print(solution(A))