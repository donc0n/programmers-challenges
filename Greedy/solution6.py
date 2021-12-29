def intersect(a, b):
    if len(a) != 2 or len(b) != 2:
        return 0
    sect = [max(a[0], b[0]), min(a[1], b[1])]
    if sect[0] > sect[1]: # 교집합이 없는 경우
        return -1
    return sect

def solution(routes): # O(rlogr + r)
    answer = 1
    routes.sort()
    last_camera = routes[0]
    for r in routes[1:]:
        camera = intersect(last_camera, r)
        if camera != -1:
            last_camera = camera
        else:
            last_camera = r
            answer += 1
    return answer