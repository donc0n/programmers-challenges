'''
섬 연결하기

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 
예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.

입출력 예
n	costs	                                    return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
'''
def solution(n, costs):
    # 크루스칼 알고리즘 O(len(costs)+n^2)
    answer = 0
    count = 0
    edges = sorted([(edge[2], edge[0], edge[1]) for edge in costs])
    parents = [i for i in range(n)]
    for cost, is1, is2 in edges:
        if parents[is1] != parents[is2]: # parent 노드가 같은 edge를 선택하면 사이클이 만들어진다.
            answer += cost
            count += 1
            p1 = parents[is1] 
            p2 = parents[is2]
            for i in range(n): # edge 선택 후 해당 parent로 병합 - 
                if parents[i] == p2:
                    parents[i] = p1
        if count == n - 1: 
            break
    return answer
        
    '''
    answer = 0
    for i in range(1, n): # O(n*len(costs))
        cost_min = 1000000 #inf
        for edge in costs: # 0번 섬에서 가장 비용이 작은 다리를 가진 섬 선택
            if 0 in edge[:2] and edge[0] != edge[1] and cost_min > edge[2]:
                cost_min = edge[2]
                island = max(edge[:2])
        answer += cost_min
        for edge in costs: # 선택한 섬을 0번 섬과 병합
            if island == edge[0]:
                edge[0] = 0
            if island == edge[1]:
                edge[1] = 0
    return answer
    '''