# 06 homework

## 1. Built-in 함수와 메서드

### sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
# .sort()
a = [1,2,5,4,3]
print(a.sort()) #None
print(a, a.sort()) #[1,2,3,4,5] None (원본만 변경)
```

```python
#sorted()
a = [1,2,5,4,3]
print(sorted(a)) #[1,2,3,4,5]
print(a, sorted(a)) #[1,2,5,4,3] [1,2,3,4,5]
```

## 2. .extend()와 .append()

### .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
#.extend()
cafe = ['starbucks', 'twosome']
drink = ['americano', 'latte']
print(cafe.extend(drink)) #['starbucks', 'twosome', 'americano', 'latte']
print(cafe.extend(['coffee'])) #['starbucks', 'twosome', 'coffee']
print(cafe.extemd('cup')) #['starbucks', 'twosome', 'c', 'u', 'p'] 
```

```python
#.append()
cafe = ['starbucks', 'twosome']
drink = ['americano', 'latte']
cafe.append(drink) #None => 프린트문 따로 해야함
print(cafe) #['starbucks', 'twosome', ['americano', 'latte']]
cafe.append('ediya')
print(cafe) #['starbucks', 'twosome', 'ediya']
```

## 3. 복사가 잘 된 건가?

### 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

```python
a = [1,2,3,4,5]
b = a
a[2] = 5
print(a)
print(b)
```

⇒ b = a 는 b의 주소에 a의 주소를 넣은 것이다.

따라서 a[2]=5로 수정을 하더라도 b도 a를 따라 수정을 하게 된다.

따라서 a == b == [1,2,5,4,5]가 된다.