#의상
# 문제 설명
# 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
# 코니는 하루에 최소 한 개의 의상은 입습니다.
# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
# 입출력
# clothes	                                                                                    return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	            3
def solution(clothes):
    # 코니는 하루에 최소 한 개의 의상을 입기 때문에 answer = 1 초기화
    answer = 1
    
    # 딕셔너리 사용
    dict = {}
    
    # 옷을 하나씩 입어본다.
    for kind in clothes:
        if kind[1] in dict:
            # 옷종류가 딕셔너리에 있으면 새로운 딕셔너리에 추가
            dict[kind[1]] += 1
        else:
            # 옷종류가 딕셔너리에 없으면 딕셔너리에 추가
            # 2를 추가하는 경우는 이거 하나만 입는 경우 떄문에 추가
            dict[kind[1]] = 2
            
    for key, value in dict.items():
        answer *= value
        
    return answer - 1 #마지막에 1개의 경우의 수 제거
A = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
#A = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
solution(A)