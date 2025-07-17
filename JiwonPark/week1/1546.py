n = int(input())

exam_list = list(map(int, input().split()))

M = max(exam_list)

sum_exam = 0

for i in range(len(exam_list)):
    exam_list[i] = exam_list[i] / M * 100
    sum_exam += exam_list[i]

print(sum_exam/n)