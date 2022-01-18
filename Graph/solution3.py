'''
방의 개수

원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

ex) 1일때는 오른쪽 위로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 하도록 solution 함수를 작성하세요.

제한사항
배열 arrows의 크기는 1 이상 100,000 이하 입니다.
arrows의 원소는 0 이상 7 이하 입니다.
방은 다른 방으로 둘러 싸여질 수 있습니다.

입출력 예
arrows	                                                    return
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	    3
'''
def solution(arrows): # 오일러 다면체 정리 v-e+f = 1 => f = e+1-v
    move = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    x , y = 0, 0
    vertices = set()
    edges = set()
    vertices.add((x, y))
    for arrow in arrows:
        # 좌표를 두 배로 만들어서 존재하지 않는 교차점까지 체크할 수 있게 한다.
        for i in range(2):
            start = (x, y)
            x += move[arrow][0]
            y += move[arrow][1]
            end = (x, y)
            vertices.add(end)
            if start <= end:
                edges.add((start, end))
            else:
                edges.add((end, start))
    answer = len(edges) + 1 - len(vertices)
    return answer
    