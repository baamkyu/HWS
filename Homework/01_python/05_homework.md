# 05 homework

## #1. 모음은 몇개나 있을까?

```python

def count_vowels(word):
    count = 0
    for i in range(len(word)): #word에 모음이 있을때마다 count = count + 1
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == ['u']:
            count = count+1
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))

```

### #2. 문자열 조작

(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.

(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다.

     특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다.

     특정 문자를 지정하지 않으면 오류가 발생한다.

# 정답 : (4) , 특정 문자를 지정하지 않아도 오류가 발생하지 않는다.

### #3. 정사각형만 만들기

```python
def only_square_area (lst1, lst2):
    square = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                square.append(lst1[i] ** 2)
    return square
print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```