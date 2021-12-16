def solution(participant, completion):
    participant.sort()
    completion.sort()
    max = len(completion)
    answer = ""
    for i in range(max):
        if (participant[i] != completion[i]):
            answer = participant[i]
            break
    if (answer == ""):
        answer = participant[max]
    return answer
    