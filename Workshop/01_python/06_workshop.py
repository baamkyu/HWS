# #1 무엇이 중복일까
# def duplicated_letters(word):
#     lst = []
#     setword = set(word)
#     for i in range(setword):
#         if int(setword.count(word[i]))>=2:
#             lst.append(word[i])
#     return lst
# print(duplicated_letters('apple'))
#1 무엇이 중복일까
def duplicated_letters(word):
    answer = set()
    for i in word:
        if word.count(i)>1:
            answer.add(i)
    return list(answer)
    
print(duplicated_letters('banana'))


#2 소대소대
def low_and_up(word):
    a = []
    for i in range(len(word)):
        if i % 2 == 1:
            a.append(word[i].upper())
        else:
            a.append(word[i].lower())
    return ''.join(a)
print(low_and_up('apple'))

#3 솔로천국 만들기
def lonely(lst):
    lst2 = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i-1] != lst[i]:
            lst2.append(lst[i])
    return lst2
print(lonely([4, 4, 4, 3, 3]))