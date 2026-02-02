# 모의고사

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

def solution(answers):
    
    arr1 = [1,2,3,4,5] 
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    answer = []
    one = 0
    two = 0
    three = 0
    
    for i in answers:
        if i == arr1[one]:
            result[0] = result[0] + 1
        if i == arr2[two]:
            result[1] = result[1] + 1
        if i == arr3[three]:
            result[2] = result[2] + 1
        one += 1
        two += 1
        three += 1
        if one == len(arr1):
            one = 0
        if two == len(arr2):
            two = 0
        if three == len(arr3):
            three = 0
            
    cnt = 1
    for i in result:
        if max(result) <= i:

            answer.append(cnt)
        cnt += 1
    return answer


A = [1,3,2,4,2]
print(solution(A))


