# 프로그래머스 
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