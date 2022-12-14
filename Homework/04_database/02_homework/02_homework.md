# 02_homework

### 1. N:1 True or False
각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오.

1. ForeignKey는 부모 테이블의 데이터를 참조하기 위한 키이다.

→ F  부모 테이블이 아닌, 외부 테이블을 참조하기 위한 키이다.

1. N:1 관계에서 1은 N의 데이터를 직접 참조 할 수 있다.

→ T 

1. on_delete 속성은 ForeignKey 필드의 필수 인자이다.

→ T

<on_delete 속성에는 여러가지가 있다.>

★ 중요! ★ CASCADE : 부모객체가 삭제되면 이를 참조하는 객체도 삭제

- PROTECT : 참조하는 객체가 있으면 삭제 불가능
- SET_NULL : 참조하는 객체를 NULL으로 바꿔줌

1. N:1 관계에서 외래 키는 반드시 부모 테이블의 PrimaryKey여야 한다.

→ F

외래키의 값이 반드시 부모테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

### 2. ForeignKey column name

다음과 같이 이름이 articles인 app의 models.py에 작성된 코드를 바탕으로 테이블이 만들어 졌을 때, 데이터베이스에 저장되는 ForeignKey 컬럼의 이름과 테이블의 이름이 무엇인지 작성하시오.

![Untitled](02_homework%20a3b60987edb4479288812c3974f0efd7/Untitled.png)

컬럼의 이름 : answer_id      ⇒ 컬럼의 이름은 변수명_id 로 생성된다.

테이블의 이름 : articles_comment    ⇒ 테이블의 이름은 앱이름_클래스명 으로 생성된다. 

### 3. N:1 model manager

위 2번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을
때, 질문(Question)에 작성된 모든 댓글(Comment)을 출력하고자 한다. 제시된 View 함수
코드를 참고하여 해당 template에서 Question 객체를 사용할 수 있다면 빈칸 __(a)__에
들어갈 알맞은 코드를 작성하시오

![Untitled](02_homework%20a3b60987edb4479288812c3974f0efd7/Untitled%201.png)

(a) : question

### 4. next parameter

다음과 같이 게시글을 삭제하는 delete 함수와 로그인을 위한 login 함수가 작성되어 있다.
만약 비로그인 사용자가 삭제를 시도한다면, django는 해당 사용자를 url에 next 파라미터가
붙은 login 페이지로 redirect 한다.
▪ /accounts/login/?next=/articles/1/delete/

1. redirect된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status
code를 작성하고, 이 오류가 발생한 원인을 작성하시오.
2. 위에서 발생한 오류를 해결하기 위해 다음과 같이 동작하는 코드로 수정하시오.
▪ 게시글 삭제는 HTTP POST method로만 가능하다.
▪ 인증되지 않은 사용자가 게시글 삭제를 시도하는 경우, 해당 게시글 상세페이지로
redirect 되도록 한다. (게시글은 삭제되지 않는다.)

![Untitled](02_homework%20a3b60987edb4479288812c3974f0efd7/Untitled%202.png)

1. @login_required는 GET 방식이어서 아래 @required_POST를 통과할 수 없다.

2)

```sql
def login(request):
	if request.user.is_authenticated:
	return redirect('articles:detail', article_pk)
...
...
```