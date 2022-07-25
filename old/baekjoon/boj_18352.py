import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readlines().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, sys.stdin.readlines().split())
    graph[a].append(b)


distance = [-1] * (n + 1)
distance[x] = 0 


q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)