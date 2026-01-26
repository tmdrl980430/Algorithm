# 프로그래머스 

### 2026-01-20
# 두 수의 연산값 비교하기 (연산)
def solution(a, b):
    answer = 0
    
    abc = str(a) + str(b)
    
    de = 2 * a * b
    
    if (de > int(abc)) :
        answer = de
    else :
        answer = int(abc)

    return answer

print(solution(91, 2))

# 원소들의 곱과 합 (조건문)
def solution(num_list):
    answer = 0
    
    a = 1 # 모든 원소들의 곱
    b = 0 # 모든 원소들의 합의 제곱
    
    for i in num_list:
        a *= i
        b += i
            
    b = b**2

    
    if (a > b) :
        answer = 0
    else : 
        answer = 1
    
    return answer

# 문자열의 앞의 n글자 (문자열)
def solution(my_string, n):
    answer = ''
    
    answer = my_string[:n]
    
    
    return answer

# 문자 리스트를 문자열로 변환하기 (문자열)
def solution(arr):
    answer = ''
    
    for i in arr:
        answer += i 
    
    return answer

# 카운트 업 (반복문)
def solution(start_num, end_num):
    answer = []
    
    for i in range(start_num, end_num+1) :
        answer.append(i)
    
    return answer

# 콜라츠 수열 만들기 (반복문)
def solution(n):
    answer = []
    
    answer.append(n)
    
    while (n != 1):
        if (n % 2 == 0):
            n /= 2
        else :
            n = 3 * n + 1
        answer.append(n)

    return answer

# 정수 찾기 (조건문 활용) 
def solution(num_list, n):
    answer = 0
    
    for i in num_list:
        if (i == n):
            answer = 1
    
    return answer
# 0 떼기 (함수(메서드))
def solution(n_str):
    answer = ''
    

    for i in n_str:
        if(n_str[0] == '0'):
            n_str = n_str[1:]
        
    answer = n_str
    
    return answer

# l로 만들기 (반복문 활용)
def solution(myString):
    answer = ''
    
    for i in myString:
        if i < "l":
            answer += "l"
        else :
            answer += i
    
    return answer


###2026-01-21 

# 주사위 게임 1 (조건문 활용)
def solution(a, b):
    answer = 0
    
    if (a % 2 == 1 and b % 2 == 1 ):
        answer += a**2 + b**2
    elif (a % 2 == 1 or b % 2 == 1 ):
        answer += 2*(a+b)
    else:
        answer = abs(a-b)
        
    return answer

# 가까운 1 찾기  (리스트(배열))
def solution(arr, idx):
    answer = -1
    
    for i in range(idx, len(arr)):
        if (arr[i] == 1):
            answer = i
            break
    
    return answer

# 수열과 구간 쿼리2 (반복문)
def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        abc = []
        a = queries[i][0]
        b = queries[i][1]
        c = queries[i][2]
        
        for j in range(a, b+1):
            if (arr[j] > c):
                abc.append(arr[j])
        
        if (len(abc) == 0):
            answer.append(-1)
        else:
            answer.append(min(abc))
            
    return answer


###2026-01-22 


# 주사위 게임3 (조건문)
# 생각 및 접근을 너무 이상하게 했다... 다음에는 더 좋은 생각으로 풀기
def solution(a, b, c, d):
    answer = 0
    diceArr = [a,b,c,d] # 입력받은 수들의 배열
    
    sumArr = [a] # 같은 숫자 몇갠지 담는 배열
    differntArr = [] # 다른 수 담는 배열
    
    for i in range(1,len(diceArr)):
        if (diceArr[i] == a):
            sumArr.append(diceArr[i])
        else:
            differntArr.append(diceArr[i])
            
    # 4개 전부 같을 때
    if (len(sumArr) == 4): 
        answer = 1111 * a
    # 초기값과 비교해서 3개 같을 때
    elif (len(sumArr) == 3): 
        answer = (10 * sumArr[0] + differntArr[0])**2             
    # 초기값과 비교해서 2개 같을 때 
    elif (len(sumArr) == 2): 
        if (differntArr[0] == differntArr[1]):  # 두개씩 같은 값
            answer = (sumArr[0] + differntArr[0]) * abs(sumArr[0] - differntArr[0])
        else:       # 두개만 같고 나머지 두개는 다른 값
            answer = differntArr[0] * differntArr[1] 
    # 초기값과 비교해서 다른 값이 3개
    else:
        # 3개 같고 1개 다름
        if (differntArr[0] == differntArr[1] == differntArr[2]):    
            answer = (10 * differntArr[0] + sumArr[0])**2    
        # 초기값과 비교해서 다른 수 2개가 같음 (1)
        elif (differntArr[0] == differntArr[1]):
            answer = sumArr[0] * differntArr[2]
        # 초기값과 비교해서 다른 수 2개가 같음 (1)
        elif (differntArr[0] == differntArr[2]):
            answer = sumArr[0] * differntArr[1]
        # 초기값과 비교해서 다른 수 2개가 같음 (1)
        elif (differntArr[1] == differntArr[2]):
            answer = sumArr[0] * differntArr[0]
        # 4개 숫자 다 다름
        elif (a != differntArr[0] != differntArr[1] != differntArr[2]):  
            answer = min(diceArr)
        
    return answer


