# 01 workshop

# 1. <img> tag

### <그림1>과 같은 폴더 구조가 있다. index.html에서 코드를 작성 중일 때, 
image 폴더 안의 my_ssafy.png를 보여주는 tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <img src="C:\Users\com\Desktop\pull_only\03_workshop\02_web\01_web_workshop\ssafy\images" alt="ssafy">
  
</body>
</html>
```

# 2. 파일 경로

### 위와 같이 경로를 (a)로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 (b)로 바꾸어 작성하면 된다.
(a)와 (b)에 들어갈 경로를 작성하시오.

- 정답 : (a) 절대 경로, (b) 상대 경로

```html
(a) img src="C:\Users\com\Desktop\pull_only\03_workshop\02_web\01_web_workshop\ssafy\images" alt="ssafy"
(b) img src="ssafy/images/my_ssafy.png" alt="ssafy"
```

# 3. Hyper Link

### 출력된 my_ssafy.png 이미지를 클릭하면 ssafy.com으로 이동하도록 코드를 수정하시오.

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
	<a href="https://ssafy.com">
	  <img src="C:\Users\com\Desktop\pull_only\03_workshop\02_web\01_web_workshop\ssafy\images" alt="ssafy">
	</a>
</body>
</html>
```

# 4. 선택자

### 1) 아래의 코드를 작성하고 결과를 확인 하시오.

```html
<div id="ssafy">
	<h2>어떻게 선택 될까?</h2>
	<p>첫번째 단락</p>
	<p>두번째 단락</p>
	<p>세번째 단락</p>
	<p>네번째 단락</p>
</div>

<style>
#ssafy > p:nth-child(2) {
color: red;
}
</style>
```

```html
<div id="ssafy">
	<h2>어떻게 선택 될까?</h2>
	<p>첫번째 단락</p>
	<p>두번째 단락</p>
	<p>세번째 단락</p>
	<p>네번째 단락</p>
</div>

<style>
#ssafy > p:nth-of-type(2) {
color: blue;
}
</style>
```

1. p:nth-child(2) {color: red;} : <p> 두번째 단락</p>가 빨간색으로 표시 됩니다.
    
    (div의 두번째 자식이자 p요소의 요건에 맞기 때문에)
    
2. p:nth-of-type(2) {color: blue;} : <p> 첫번재 단락 </p>가 파란색으로 표시 됩니다.
    
    (div의 자식이면서 같은 유형 두번째 p이기 때문에)
    
- **nth-child**와 **nth-of-type**의 가장 큰 차이점은 바로 해당하는 태그의 순서를 말하는지 아니면 부모 속성에서 특정 태그를 가진 자식 속성에서 몇번째 해당하는지의 차이다.
    - nth-child : 모든 자식의 순서에서 찾음
    - nth-of-type: 해당하는 자식 태그 요소에서의 순서를 찾음