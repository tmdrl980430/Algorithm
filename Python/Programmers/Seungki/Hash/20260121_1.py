# 베스트앨범
# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

def solution(genres, plays):
    answer = []
    dict = {}
    genres_dict = {}
        
    for i in range(len(genres)):
        # 장르별 딕셔너리를 만들어준다.
        # 장르별 재생된 횟수를 추가해준다.
        if genres[i] in dict:
            dict[i] += plays[i] 
        else:
            dict[i] = plays[i]
        
        # 장르별 고유번호가 같은 것들만 넣어준다.
        if genres[i] in genres_dict:
            genres_dict[genres[i]] += plays[i]
        else:
            genres_dict[genres[i]] = plays[i]  

    #정렬한다
    genres_dict = sorted(genres_dict.items(), key = lambda item: item[1], reverse = True)
    dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    
    for key , value in genres_dict:
        count = 0
        for keys, values in dict:

            if key == genres[keys] and count < 2:
                answer.append(keys)
                count += 1
            if count == 2:
                count = 0
                break
    return answer

A = ["classic", "pop", "classic", "classic", "pop"]
B = [500, 600, 150, 800, 2500]
print(solution(A, B))