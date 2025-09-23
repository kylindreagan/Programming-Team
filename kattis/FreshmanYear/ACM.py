questions = {}
right = {}

while True:
    temp = input()
    if temp == "-1":
        break
    curr_score, ques, correct = temp.split()
    curr_score = int(curr_score)
    correct = correct == "right"
    if ques not in questions:
        questions[ques] = 0
    if correct:
        right[ques] = questions[ques] + curr_score
    else:
        questions[ques] += 20

print(len(right), sum(right.values()))