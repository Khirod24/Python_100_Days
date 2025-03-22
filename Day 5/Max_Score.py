student_scores  = input().split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

maximum_score = 0
for score in student_scores:
    if score>maximum_score:
        maximum_score = score

print(f"The highest score is = {maximum_score}") 