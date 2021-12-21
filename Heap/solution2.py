'''
디스크 컨트롤러

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. 
(단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

입출력 예
jobs			return
[[0, 3], [1, 9], [2, 6]]	9
'''
def solution(jobs):
    import heapq as hq
    sec = 0
    work = 0
    answer = 0
    i = 0
    heap = []
    jobs.sort()
    while True:
        if not work and not heap and i >= len(jobs):
            break
        while i < len(jobs): # 요청 시간에 맞춰서 작업 대기 영역으로 옮김
            if sec == jobs[i][0]:
                hq.heappush(heap, (jobs[i][1], jobs[i][0]))
                i += 1
            else:
                break
        if work == 0: # 작업이 없다면 대기 영역에서 작업을 가져와 시작
            if heap: 
                work, req = hq.heappop(heap)
        sec += 1
        if work > 0: # 작업 중이라면 작업을 1ms 수행
            work -= 1
            if work == 0: # 작업이 완료된 경우 작업의 요청부터 종료까지 걸린 시간 계산
                answer += (sec - req)
    return answer // len(jobs) # 왠지 모르겠지만 소수값이 리턴된다. 버려주자.
