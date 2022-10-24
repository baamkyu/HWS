# 02_workshop

### 1. 주어진 문자열이 회문인지 판별하는 isPalindrome함수를 완성하시오.

```jsx
function isPalindrome(str) {
  const noSpaceStr = str.replaceAll(' ', '')  // 공백 지우기 -> google
  const arr = noSpaceStr.split('') // 한글자씩 나눠서 리스트로 -> ['g','o'....]
  arr.reverse()
  const reverseStr = arr.join('') // 뒤집어진 애를 문자열로 합쳐줌 -> elgoog
  return noSpaceStr === reverseStr
}

console.log(
  isPalindrome('a santa at nasa'),  // true
  isPalindrome('google')  // false
)
```