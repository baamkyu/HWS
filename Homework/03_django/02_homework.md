# 02_homework

## 1. Model 반영하기

“Django가 Model에 생긴 변화를 DB에 반영하는 방법” 을 뜻하는 용어를 작성하시오.

- Migrations (마이그레이션)

> Migrations 관련 주요 명령어
> 
- makemigrations
- migrate

> makemigrations
> 
- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도)를 만들 때 사용
- 테이블을 만들기 위한 설계도를 생성하는 것
- 명령어 실행 후 migrations/0001_initial.py가 생성된 것을 확인
- “파이썬으로 작성된 설계도”

```python
$ python manage.py makemigrations
```

> migrate
> 
- makemigrations로 만든 설계도를 실제 db.sqlite3 DB 파일에 반영하는 과정
- 결과적으로 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸
- “모델과 DB의 동기화”

```python
$ python manage.py migrate
```

## 2. Model 변경사항 저장하기

```python
class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```

1. 위에서 작성한 Model의 변경사항을 저장하기 위한 명령어를 작성하시오.
    
    ```python
    article = Article()
    --- 변경사항 입력 ---
    article.save()    
    
    # save 메서드를 호출해야 비로소 DB에 데이터가 저장된다. (레코드 생성)
    ```
    
    1. 이로 인해 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과를 작성하시오. (app의 이름은 articles이다.)
    
    ```python
    $ python manage.py sqlmigrate articles0001
    ```
    

## 3. Python Shell

Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떤 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.

```python
$ python manage.py shell_plus
```

> Shell   ( 껍데기 )
> 
- 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
- 셸은 사용자와 운영 체제의 내부사이의 인터페이스를 감싸는 층이기 때문에 그러한 이름이 붙음
- “사용자 ↔ 셸 ↔ 운영체제”

> Python Shell ⇒ IDLE이 Python Shell인가(?)
> 
- 파이썬 코드를 실행해주는 인터프리터
    - 인터프리터 : 코드를 한 줄 씩 읽어 내려가며 실행하는 프로그램
- Python 명령어를 실행하여 그 결과를 바로 제공

> Django Shell
> 
- ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
- 다만, 일반 파이썬 쉘은 장고 프로젝트 환경에 영향을 줄 수 없기 때문에 Django환경 안에서 진행할 수 있는 Django 쉘을 사용
- python [manage.py](http://manage.py) shell_plus

## 4. Django Model Field

Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

⇒ Django Model Field 구글 검색 후, Django 홈페이지 참고

![Untitled](02_homework%20f8be60dafcca456c91c4c716c5dacdb3/Untitled.png)

![Untitled](02_homework%20f8be60dafcca456c91c4c716c5dacdb3/Untitled%201.png)