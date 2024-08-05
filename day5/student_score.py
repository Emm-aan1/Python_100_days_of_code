student_scores = [78, 63, 52, 84, 92, 73, 79, 67, 93, 85, 65]
highest_score = 0
lowest_score = 100

for score in student_scores:
    if score > highest_score:
        highest_score = score

    if score < lowest_score:
        lowest_score = score

print("The highest score is: ", highest_score)
print("The lowest score is: ", lowest_score)
