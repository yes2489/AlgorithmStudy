n = int(input())

scores = list(map(int, input().split()))

m = max(scores)

new_scores = list(map(lambda x: x / m * 100, scores))

average = sum(new_scores) / len(new_scores)

print(average)
