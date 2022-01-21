'''
순위

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.

입출력 예
n	results	                                    return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	    2

입출력 예 설명
2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.
'''
def solution(n, results): # O(V*V + E)
    # 확실한 순위 i위가 되기 위해서는 i-1개의 노드들에게 lose해야 하고 n-i개의 노드들에게 win해야 한다
    # win 방향 탐색, lose방향 탐색 만으로 모든 노드에 도달 가능해야 한다.
    answer = 0
    win_adjs = [[] for i in range(n+1)]
    lose_adjs = [[] for i in range(n+1)]
    for winner, loser in results:
        win_adjs[loser].append(winner)
        lose_adjs[winner].append(loser)
    for i in range(1, n+1):
        stack = [i]
        visited = [0 for j in range(n+1)]
        visited[0] = 1
        visited[i] = 1
        while(stack):
            q = stack.pop()
            for winner in win_adjs[q]:
                if not visited[winner]:
                    visited[winner] = 1
                    stack.append(winner)
        stack = [i]
        while(stack):
            q = stack.pop()
            for loser in lose_adjs[q]:
                if not visited[loser]:
                    visited[loser] = 1
                    stack.append(loser)
        if sum(visited) == n+1:
            answer += 1
    return answer
    