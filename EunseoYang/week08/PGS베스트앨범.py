def solution(genres, plays):
    
    # 각 장르의 총 재생수
    genreTotal = {}
    for g, p in zip(genres, plays):        # (장르, 재생수) 쌍으로 순회
        genreTotal[g] = genreTotal.get(g, 0) + p  # 누적 (없으면 0에서 시작)
    
    # 각 장르별 노래 리스트
    genreSongs = {} # 장르: [{인덱스, 재생 수}]
    for i, g in enumerate(genres): # enumerate(): 시퀀스를 돌 때, 인덱스와 값 둘 다 한 번에 꺼내주는 내장 함수
        p = plays[i] # 인덱스 바로 맞춰서 play값 꺼내오기
        if g not in genreSongs: # 기존에 없는 장르면 리스트에 추가
            genreSongs[g] = []
        genreSongs[g].append((i, p))
        
    # 장르 내부 정렬: 재생수 내림 차순, 동률이면 인덱스 오름차순        
    for g in genreSongs:
        genreSongs[g].sort(key=lambda x: (-x[1], x[0]))
    
    # 장르들을 총 재생수 기준으로 내림차순 정렬
    genreOrder = sorted(genreTotal.items(), key=lambda x: x[1], reverse=True)

    res = []
    for g, _ in genreOrder:
        # 해당 장르의 노래 목록 꺼내기
        songs = genreSongs[g]
        
        # 베스트앨범에는 한 장르당 최대 2곡까지 수록 가능
        for idx, _ in songs[:2]:
            res.append(idx)
    
    return res
