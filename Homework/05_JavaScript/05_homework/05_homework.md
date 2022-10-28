# 05_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다. → T
- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다. → F
    
    → 이유 : Task Queue에서 대기하다가 Call Stack이 비워졌을 때 할당된다.
    

### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- 동기 함수 : 모든 일을 순서대로 하나씩 처리하는 것.
- 비동기 함수 : 결과를 기다리지 않고 다음 작업을 처리하는 것.
    
    동기 함수는 앞의 작업이 끝나지 않으면 그 후의 작업들을 할 수 없다, 하지만 비동기 함수는 앞의 작업이 오래걸리더라도 그 동안 그 후의 작업들을 먼저 할 수 있다.
    

### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

![Untitled](05_homework%20f138f9a8da83471e969b41960744f109/Untitled.png)

(a) get  (b) then  (c) response.data