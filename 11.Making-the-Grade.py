def round_scores(student_scores):
    list1 = []
    for score in student_scores:
        list1.insert(0 , round(score))

    return list1

def count_failed_students(student_scores):
    x = 0
    for score in student_scores:
        if score <= 40:
            x+=1
    return(x)

def above_threshold(student_scores, threshold):
    list1 = []
    for scores in student_scores:
        if scores >= threshold:
            list1.append(scores)

    return list1

def letter_grades(highest):
    divided_score = round((highest-40)/4)
    list1 = []
    for number in range(40, highest, divided_score):
        if number >= 40 and number < highest-1:
            list1.append(number+1)
    return list1

def student_ranking(student_scores, student_names):
    list1 = []
    for index, names in enumerate(student_names):
        list1.append(f"{index+1}. " f"{student_names[index]}" ":" f" {student_scores[index]}")
    return list1

def perfect_score(student_info):
    list1 = []
    for info in student_info:
        if info[1] == 100:
            return info
    return list1

print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))



