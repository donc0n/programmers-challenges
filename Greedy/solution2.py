'''
조이스틱

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.

따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
'''
def solution(name):
    updowns = 0
    count = 0
    max_A = 0
    end_A = len(name)
    for i, n in enumerate(name):
        updowns += min((26 - ord(n) + 65), (ord(n) - 65)) # 위아래 방향 최소 이동 계산
        # 연속되는 A문자열의 최대 반복횟수max_A와 해당 끝 위치end_A 계산 
        if i == 0:
            continue
        if n == "A":
            count += 1
        else:
            if count > max_A:
                max_A = count
                end_A = i
            count = 0 # name이 A로 끝나면 count는 name의 끝부터 연속되는 A문자열의 길이
    '''
    min(CASE 1, CASE 2, CASE 3)
    CASE 1: BBABBB
    CASE 2: BBBBAB
    CASE 3: BABAA
    '''
    return updowns + len(name) + min((end_A - 2*max_A - 2), (len(name) - end_A - max_A - 1), (- 1 - count))
    