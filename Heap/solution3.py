'''
이중우선순위큐

이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	    큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 
비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

제한사항
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

입출력 예
operations	                return
["I 16","D 1"]	            [0,0]
["I 7","I 5","I -5","D -1"]	[7,5]
'''
import heapq as hq
class Dpq:
    def __init__(self):
        self.heap = [] # 최소 힙
    def push(self, value):
        hq.heappush(self.heap, value)
    def pop_min(self):
        if not self.heap:
            return "error1"
        return hq.heappop(self.heap)
    def pop_max(self): # 최소 힙을 최대 힙으로 만들어 최대값을 pop한 후 최소힙을 돌려놓는다.
        if not self.heap:
            return "error2"
        self.heap = list(map(lambda x: -x, self.heap))
        hq.heapify(self.heap)
        max_val =  -hq.heappop(self.heap)
        self.heap = list(map(lambda x: -x, self.heap))
        hq.heapify(self.heap)
        return max_val
    def __len__(self):
        return len(self.heap)
    def min(self):
        return min(self.heap)
    def max(self):
        return max(self.heap)

def solution(operations):
    dpq = Dpq()
    answer = []
    for op in operations: # 명령어 파싱
        args = op.split(" ")
        if args[0] == 'I':
            dpq.push(int(args[1]))
        elif args[0] == 'D':
            if args[1] == '-1':
                dpq.pop_min()
            elif args[1] == '1':
                dpq.pop_max()
    if len(dpq) == 0:
        return [0, 0]
    return [dpq.max(), dpq.min()]
