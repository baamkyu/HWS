# 07 homework

## 1. Type Class

### Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

- int, float, str(문자열), dict(딕셔너리), list(리스트), tuple(튜플) 등

## 2. Magic Method

### 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

```python
__init__, __del__, __str__, __repr__ 
```

- __init__: 우리가 보통 생성자라고 부르는 메서드. 데이터 초기화 하는 등의 목적으로 사용.
- __del__: 객체가 소멸될 때 호출되는 메서드
- __str__, __repr__: 객체의 문자열 표현을 위해 사용되는 메서드

## 3. Instance Method

### .sort() 와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.

- .append() : 리스트에 데이터를 추가하는 메서드
- .join() : 문자로 구성된 리스트를 문자열로 바꾸어주는 메서드
- .split(’a’) : 괄호 안의 문자를 기준으로 앞 뒤를 나누는 메서드
- .strip() : 공백 제거해주는 메서드
- .lower() : 문자열을 소문자로 변환시키는 메서드
- .upper() : 문자열을 대문자로 변환시키는 메서드
- .islower() : 해당 문자가 소문자인지 확인시키는 메서드
- .isupper() : 해당 문자가 대문자인지 확인하는 메서드

## 4. 오류의 종류

### 아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

```python
ZeroDivisionError, NameError, TypeError, IndexError,
KeyError, ModuleNotFoundError, ImportError
```

- ZeroDivisionError : 0으로 나누려는 경우에 발생하는 에러.
    - ex) a = 99/0        print(a)
- NameError : 변수 이름을 찾을 수 없는 경우에 발생하는 에러.
    - ex) a=1     b=2     print(c)
- TypeError : 잘못된 타입을 전달했을 때 발생하는 에러.
    - ex) a=1+”abc”
- IndexError : 인덱스 범위를 벗어나는 경우에 발생하는 에러.
    - ex) arr = [’a’,’b’,’c’]    print(arr[10])
- KeyError : 딕셔너리에서 접근하려는 키값이 없을 때 발생하는 에러.
    - ex) a={”a”:1, “b”:2}   result = a[”z”]
- ModuleNotFound : 모듈에 접근하려고 할 때, 해당 모듈이 없는 경우 발생하는 에러.
- ImportError : import 할 때 나는 오류