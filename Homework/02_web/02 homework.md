# 02 homework

# 1. Semantic Tag

### 보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱(semantic)태그를 모두 고르시오.

```html
div, header, h1, section, footer, a, form, span
```

- 정답 : header, h1, section, footer, a, form

# 2. input Tag

### 아래 이미지와 같이 로그인 Form을 생성하는 HTML코드를 작성하오. 단, USERNAME 글자를 클릭하면 아이디를 입력하는 input에, PWD 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 되도록 하시오.

```html
<body>
    <label for="username">USERNAME : </label>
    <input type="text" name="username" id="username" value="아이디를 입력 해 주세요."><br>
    <label for="password">PWD : </label>
    <input type="text" name="password" id="password">
    <button>로그인</button>
</body>
```

# 3. 크기 단위

### 크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

- 정답 : rem

# 4. 선택자

### 다음 예제를 통해 ‘자손 결합자’와 ‘자식 결합자’의 차이를 설명하시오.

```html
/* 자손 결합자 */
div p {
	color : crimson;
}

/* 자식 결합자 */
div >p {
	color : crimson;
}
```

- div p 자손 결합자는 div 하위에 존재하는 p 라는 조건을 달고 해당하는 모든 p 에게 아래 스타일을 덮어씌운다는 뜻이다.
반면에, div > p는 div 바로 아래에 p가 존재할 때, style을 적용하겠다는 뜻이다.