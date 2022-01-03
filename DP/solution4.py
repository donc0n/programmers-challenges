'''
도둑질

도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

제한사항
이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

입출력 예
money	        return
[1, 2, 3, 1]	    4
'''
def solution(money):
    # O(n)이 되어야 풀 수 있다.
    n = len(money)
    dp = [[0,0] for i in range(n)]
    # 첫 번째 집을 선택한 경우
    dp[n-2][1] = money[n-2]
    dp[n-3][1] = max(money[n-3], dp[n-2][1])
    for i in range(n-4, 1, -1):
        dp[i][1] = max(money[i]+dp[i+2][1], dp[i+1][1])
    dp[0][1] = money[0] + dp[2][1]
    # 첫 번째 집을 선택하지 않은 경우
    dp[n-1][0] = money[n-1]
    dp[n-2][0] = max(money[n-2], dp[n-1][0])
    for i in range(n-3, 0, -1):
        dp[i][0] = max(money[i]+dp[i+2][0], dp[i+1][0])
    dp[0][0] = dp[1][0]
    return max(dp[0][0], dp[0][1])
'''
def solution(money): # 재귀함수 버전
    # O(n)이 되어야 풀 수 있다.
    global n
    global moneys
    n = len(money)
    moneys = money
    return dp(0)

first_select = False
cache = [[-1,-1] for i in range(1000001)]
moneys = []

def dp(idx):
    global first_select
    global cache
    global moneys
    global n
    if idx >= n:
        return 0
    elif idx == n-1 and first_select == True:
        return 0
    ret = cache[idx][first_select]
    if ret != -1:
        return ret
    if idx == 0:
        first_select = False
    ret = max(ret, dp(idx+1))
    if idx == 0:
        first_select = True
    ret = max(ret, moneys[idx] + dp(idx+2))
    cache[idx][first_select] = ret
    return ret
'''
