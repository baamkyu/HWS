# 05_homework

## 1. Django User Model

Django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다.

```python
from django.contrib.auth.models import User
```

Django 공식 github에서 User모델이 정의된 코드를 찾아본 후 우리가 User모델을 대체 시 AbstractUser를 상속 받는 부모 클래스로 설정한 이유를 작성해보시오.

- default값을 사용하면 원하는 값을 설정하지 못해, custom해주는 것이다.

<Django user 모델 확장의 4가지 방법>
Proxy Model: 기존의 User 모델을 그대로 사용하되, 일부 동작을 변경하는데만 사용
User Profile: 하나의 새로운 모델을 정의한 후, User 모델과 1:1 관계설정(프로필 모델 참조)
AbstractBaseUser: 완전한 새로운 User 모델을 만들때 사용
AbstractUser: 기존의 User 모델을 사용하되, 추가적인 정보를 더 넣고 싶을 때 사용

2번 방법은 추가로 클래스를 생성하지만, 이 방법의 경우 추가로 클래스를 생성하지는 않음.

## 2. Create user by ModelForm

새 유저를 생성하기 위해서 Django 내부에 정의된 ModelForm을 사용하려 한다. 이 때 유저 생성 form을 사용하기 위해 작성하는 import 구문을 적으시오.

```python
from django.contrib.auth.forms import UsercreationForm
```

## 3. Django sessions

Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다.

그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다.

(a)와 (b)에 알맞은 값을 작성하시오.

(a) django_session

(b) session id