# 완주하지 못한 선수
def solution(participant, completion):
    # 참가자 등장 횟수 세기
    part_dict = {}
    for p in participant:
        if p in part_dict:
            part_dict[p] += 1
        else:
            part_dict[p] = 1

    # 완주자 등장 횟수 빼기
    for c in completion:
        part_dict[c] -= 1

    # value가 1인 key가 완주하지 못한 사람
    for name, count in part_dict.items():
        if count == 1:
            return name
