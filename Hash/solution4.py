"""
베스트앨범

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
"""
def solution(genres, plays):
    from functools import reduce
    id_genres = {genre: [] for genre in set(genres)}
    for index, genre in enumerate(genres): # 곡 번호들을 각 장르별로 해싱
        id_genres[genre].append(index)
    id_genres = list(zip(id_genres.keys(),id_genres.values()))
    for genre, id_list in id_genres: # 장르별 곡 번호 정렬
        id_list.sort(key = lambda x: plays[x], reverse = True)
    id_genres.sort(key = lambda x: sum(map(lambda y: plays[y], x[1])), reverse = True) # 장르 정렬
    answer = []
    for genre, id_list in id_genres:
        answer.append(id_list[0])
        if len(id_list) > 1: # 곡의 수가 두 개가 되는지 체크
            answer.append(id_list[1]) 
    return answer
    