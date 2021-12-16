from collections import Counter as c 

def solution(clothes):
    types = [cloth[1] for cloth in clothes]
    types_c = c(types)   
    answer = 1
    for count in list(types_c.values()):
        answer = answer * (count+1)
    
    return answer - 1
    