# 단지번호붙이기

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
result = []

each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0 <= ny < N and 0 <= nx < N :
            if map[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                dfs(ny, nx)
    
    
    
for j in  range(N):
    for i in range(N):
        if map[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)
            #방문 체크 표시
            #DFS 로 크기 구하기
            #크기를 결과 리스트에 넣기

result.sort()
print(len(result))
for i in result:
    print(i)