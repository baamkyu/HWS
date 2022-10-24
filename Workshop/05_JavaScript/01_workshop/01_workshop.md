# 01_workshop

### 제공된 workshop01.js 파일을 따라 개발자 도구 Console에서 직접 입력해보시오.

```jsx
/*
  [let 키워드 연습]
  
  1. let 키워드를 이용하여 firstName 변수를 작성하세요.
  2. firstName 변수에 여러분의 이름을 할당하세요.
  3. firstName 변수의 값을 다른 이름으로 재할당하세요.
*/

let firstName
> undefined

firstName = 'lim'
> 'lim'

firstName = 'kim'
> 'kim'
```

```jsx
[const 키워드 연습]
  
/*
  1. const 키워드를 이용하여 lastName 변수를 작성하세요.
  2. lastName 변수에 여러분의 이름을 할당하세요.
  3. lastName 변수의 값을 다른 이름으로 재할당하세요.
  4. 재할당 에러를 확인하세요.
*/

const lastName = 'lim bk'
> undefined

lastName
> 'lim bk'

lastName = 'kim aa'
> Uncaught TypeError: Assignment to constant variable.
    at <anonymous>:1:10

```

```jsx
/*
  [블록 스코프 <-> let 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

let fullName = 'Brendan Eich'

if (true) {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName) // Guido Van Rossum
}

console.log('전역 스코프:', fullName) // Brendan Eich
```

`★ Python과의 차이점 : Java Script에는 블록스코프, 전역스코프가 있다!`

```jsx
/*
  [var 키워드 연습]
  
  1. var 키워드를 이용하여 framework 변수를 작성하세요.
  2. framework 변수에 'Bootstrap'를 할당하세요.
  3. framework 변수에 'Django'를 재할당하세요.
  4. framework 변수를 재선언하고 'Vue'를 할당하세요.
*/

var framework
framework = 'Bootstrap'
console.log(framework)  // Bootstrap

framework = 'Django'
console.log(framework)  // Django

var framework = 'Vue'
console.log(framework)  // Vue
```

```jsx
/*
  [함수 스코프 <-> var 키워드 예시]

  아래 코드 실행 후 결과를 확인해보세요.
*/

function f1() {
  var message = 'You are doing great!'
}
f1()
console.log(message) // ReferenceError: message is not defined
```

```jsx
/*
  [블록 스코프 <-> var 키워드 예시]

  Tip. if문은 블록 스코프를 생성합니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme) // 'dark+'
```

`var는 함수스코프에서만 못나오고, const랑 let은 블록스코프, 함수스코프 다 못나온다!!`

```jsx
/*
  [블록 스코프 <-> const, let 키워드 예시]
  
  Tip. 
    const와 let은 블록 스코프입니다.
    함수의 중괄호도 블록에 해당됩니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

function f2() {
  const stack = 'Last In, First Out'
}
f2()
console.log(stack) // ReferenceError: stack is not defined

function f3() {
  let queue = 'First In, First Out'
}
f3()
console.log(queue) // ReferenceError: queue is not defined

function f4() {
  var a = 'abc'
}
f4()
console.log(a) // ReferenceError: a is not defined
```

```jsx
/*
  [호이스팅(hoisting)]
  
  아래 코드 실행 후 결과를 확인해보세요.
  그리고 const와 let의 경우와 비교해보세요.
  
*/

// 두줄을 동시에 console에 입력해야 합니다.
console.log(hoisted) // undefined
var hoisted = 'can you see me?'

console.log(lunch) // ReferenceError
const lunch = '초밥'

console.log(dinner) // ReferenceError
let dinner = '스테이크'
```