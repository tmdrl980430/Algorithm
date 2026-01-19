#Test

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
    cnt = 0
    for item in  arr:
        if cnt == 0 :
            answer.append(item)
            cnt += 1
            continue
        
        if answer[cnt-1] != item:
            answer.append(item)
            cnt += 1
        
    return answer
