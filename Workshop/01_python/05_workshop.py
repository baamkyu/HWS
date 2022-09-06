def get_dict_avg(student):
    scores = []
        for i in student.values:
            scores.append(i)
        result = sum(scores) / len(student)
    return result

#2 혈액형 분류하기
def count_blood(abc):
    a = []
    for i in abc:
        a.append(abc[i])


count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB',
'O', 'A', 'B', 'O', 'B', 'AB',
]) # => {'A': 3, 'B': 3, 'O': 3, 'AB': 3