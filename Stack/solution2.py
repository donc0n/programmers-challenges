'''
프린터

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

입출력 예
priorities	        location	return
[2, 1, 3, 2]	        2	       1
[1, 1, 9, 1, 1, 1]	    0	       5
'''
def solution(priorities, location):
    answer = 0 # 중요도 몇 번째인지 계산
    last = 0 # 가장 최근에 대기목록에서 꺼낸 인덱스 번호
    max = len(priorities)
    for pivot in range(9,0,-1):
        for i in list(range(last, max)) + list(range(0, last)):
            if priorities[i] == pivot: # 중요도가 일치하면 작업을 꺼낸다
                answer = answer + 1
                if i == location:
                    return answer
                last = i
    return -1 # 예외 처리
