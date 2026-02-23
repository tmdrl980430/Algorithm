# 소수 찾기 
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# "17"	    3
# "011"	    2




import itertools

def solution(numbers):
    answer = 0
    
    arr = list(numbers)
    print(list(arr))
    print(len(arr))
    arr2 = []
    
    # 순열 생성 (각 숫자의 대한 조합)
    for r in range(1, len(arr) + 1):
        for p in itertools.permutations(arr, r):
            arr2.append("".join(p))
    
    result = []
    # 앞이 0인거는 빼야함
    for i in arr2:
        if i[0] == "0":
            continue
        else:
            if i not in result:
                result.append(i)
    
    for n in result:
        if is_prime(int(n)):
            answer +=1
    print(list(result))

    return answer

# 소수인지 판별하는 함수
def is_prime(n):
    
    # 2보다 작을 경우는 소수가 아님 ex)1
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    # 반복문 설명
    # 반복문의 조건은 2*2, 3*3, 4*4.... 보다  크다면 나눠볼 필요가 없음.
    return True