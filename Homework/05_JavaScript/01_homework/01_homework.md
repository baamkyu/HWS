# 01_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한
차이점은 변수의 유효범위이다. → F
    - let : 재할당 가능, 재선언 불가능
    - const : 재할당 불가능, 재선언 불가능
    - var : 재할당 가능, 재선언 가능
    
- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산
자에서 undefined가 반환된다. → F
    
    → null은 object, undefined는 undefined 출력
    
- for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로
활용한다. → F
    
    → for … in 문은 index 번호를 출력, 각 요소를 순회하려면 for … of 문을 사용해야 한다.
    
- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true
아니면 false를 반환한다. → F
    
    → 값이 똑같은지 확인하려면 ‘===’을 사용한다. (python의 ‘==’와 동일)
    

### 2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오.

```jsx
const numbers = [1, 2, 3, 4, 5]
```

- for … of 문을 사용하여 배열의 각 요소를 출력하시오.

```jsx
for (const number of numbers) {
	console.log(number)
}
```

- for … of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생성하시오.

```jsx
const plusTenNumber = []
for (const number of numbers) {
	plusTenNumber.push(number + 10)
}
console.log(plusTenNumber)
```

- for … of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생성하시오.

```jsx
const oddNumbers = []
for (const number of numbers) {
	if (number % 2 === 1) {
		oddNumbers.push(number)
	}
}
console.log(oddNumbers)
```

- for … of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오

```jsx
let hap = 0
for (const number of numbers) {
	hap += number
}
console.log(hap)
```