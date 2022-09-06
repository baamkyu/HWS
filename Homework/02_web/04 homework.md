# 04 homework

# 1. CSS flex-direction

### flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

1) row : 주 축을 행으로 설정한다 (기본 방향: 좌→우)

2) row-reverse : 행의 방향을 바꾼다 (우→좌)

3) column : 주 축을 열로 설정한다 (기본 방향: 상→하)

4) column-reverse : 열의 방향을 바꾼다 (하→상)

# 2. Bootstrap flex-direction

### flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

1) flex-direction: row; -> flex-row
2) flex-direction: row-reverse; -> flex-row-reverse
3) flex-direction: column; -> flex-column
4) flex-direction: column-reverse; flex-column-reverse

# 3. align-items

### align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

1) stretch : 글자를 쭉 늘려준다

2) flex-start : 글자를 첫째 줄에 놔준다

3) flex-end : 글자를 마지막 줄에 놔준다

4) center : 글자를 중간에 놔준다

# 4. flex-flow

### flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것은?

```html
(1) flex-direction, flex-wrap
(2) flex-direction, align-items
(3) justify-content, flex-wrap
(4) justify-content, align-items
```

(1) flex-flow는 flex-direction, flex-wrap의 shorthand이다.

flex-direction, flex-wrap에 대한 설정 값을 차례로 작성. ex) flex-flow: row nowrap;

(flex-direction : 주 축 기준 방향 설정

flex-wrap : 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정. 즉, 컨테이너 영역을 벗어나지 않도록 함)

# 5. Bootstrap Grid System

### 상단 코드에 Bootstrap Grid System을 적용시키고자한다. (a), (b) 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class=" ">
	<div class=" ">
		<div class="col- - "></div>
	</div>
</div>
```

(a) : container

(b) : row

# 6. Breakpoint prefix (5번 연계)

### Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

1)  (c)에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.

(c) : col-{breakpoint} : 화면의 크기가 줄어들 때 어떤 범위에서 변화할지 설정

.col- : <576px
.col-sm : ≥576px
.col-md : ≥768px
.col-lg : ≥992px
.col-xl : ≥1200px
.col-xxl : ≥1400px

2)  (d)에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.

(d) : {n} (숫자) : 

12개의 칼럼중 몇개의 공간을 차지할지 결정
12이상 부터는 한줄을 차지함.