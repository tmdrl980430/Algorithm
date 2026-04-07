# 풀이를 작성하세요
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
MAX = 100001

matrix = [[] for _ in range(N+1)]
distance = [float("inf")] * (N+1)
distance[S] = 0

for i in range(M):
    start, end , weight = map(int, input().split())
    matrix[start].append((end, weight))
P = int(input())
P_list = []
for i in range(P):
    node = int(input())
    P_list.append(node)

def dijkstra(start):
    queue = [(0, start)]

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        
        if cur_dist > distance[cur_node]:
            continue
        for end, w in matrix[cur_node]:
            cost = cur_dist + w
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(queue, (cost, end))
    return distance

dijkstra(S)
result = False

for i in P_list:

    if distance[i] == float("inf"):
        continue
    else:
        result = True
print(distance[E])

if result:
    print("YES")
else:
    print("NO")


