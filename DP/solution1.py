"""
N으로 표현

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

입출력 예
N	number	return
5	    12	     4
2	    11	     3
"""
def operation(A, B):
    # 사칙연산 + - * /
    if A != 0 and B != 0:
        return list(filter(lambda x: x != 0, [A+B, A-B, B-A, A*B, A//B, B//A]))
    else:
        return -1

def solution(N, number): # O(1)
    # _N[i]는 N을 i번 써서 만들 수 있는 숫자들의 집합
    _N = [{}] + [set([int(str(N)*i)]) for i in range(1,9)] # N, NN, NNN, NNNN... 인 경우      
    for i in range(1, 9): # _N[i] generate   
        for j in range(1, i//2 + 1):
            for A in _N[j]:
                for B in _N[i-j]:
                    for res in operation(A, B):
                        _N[i].add(res)
        if number in _N[i]:
            return i
    return -1

# _N[4] = (_N[1] op _N[3]) + (_N[2] op _N[2]) 
# 연산에 대한 교환성을 생각해야 함
# 처음 초기화한 값들(N, NN, NNN...)에 대해서도 값 검증을 해야 함
