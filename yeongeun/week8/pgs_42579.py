# 베스트앨범
from collections import Counter

def solution(genres, plays):
    play_cnt_by_genre = Counter()
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        play_cnt_by_genre[genre] += play

        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))

    # 장르별 노래 정렬
    for genre in genre_songs:
        genre_songs[genre].sort(key=lambda x: (-x[0], x[1]))

    # 장르 정렬
    sorted_genres = [genre for genre, _ in play_cnt_by_genre.most_common()]

    # 결과값 생성
    answer = []
    for genre in sorted_genres:
        top_songs = genre_songs[genre][:2]
        answer.extend([song[1] for song in top_songs])

    return answer
