"""
완주하지 못한 선수

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    max = len(completion)
    answer = ""
    # 두 정렬된 리스트에서 불일치 하는 부분이 정답
    for i in range(max):
        if (participant[i] != completion[i]):
            answer = participant[i]
            return answer
    if (answer == ""):
        answer = participant[max]
        return answer
    