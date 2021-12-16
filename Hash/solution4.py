def solution(genres, plays):
    from functools import reduce
    id_genres = {genre: [] for genre in set(genres)}
    for index, genre in enumerate(genres): # 곡 번호들을 각 장르별로 해싱
        id_genres[genre].append(index)
    id_genres = list(zip(id_genres.keys(),id_genres.values()))
    for genre, id_list in id_genres:    # 장르별 곡 번호끼리의 정렬
        id_list.sort(key = lambda x: plays[x], reverse = True)
    id_genres.sort(key = lambda x: sum(map(lambda y: plays[y], x[1])), reverse = True)      # 장르끼리의 정렬
    answer = []
    for genre, id_list in id_genres:
        answer.append(id_list[0])
        if len(id_list) > 1:
            answer.append(id_list[1]) 
    return answer
    