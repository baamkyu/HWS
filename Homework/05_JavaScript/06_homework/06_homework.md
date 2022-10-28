# 06_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로
할당하는 역할을 한다. → T
- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.
XHR객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다. → F
    
    → 이유 : Web API가 아니고 JAVA Script API이다.
    
- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는
라이브러리이다. → T

### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

![Untitled](06_homework%2034e22ce04fa946f0b92ec63c4f8cf77e/Untitled.png)

1. Hello SSAFY를 Call Stack으로 보낸다.
2. 대기시간이 없으므로 바로 출력해준다.
3. I am from setTimeout을 Call Stack으로 보낸다.
4. 대기시간이 있으므로 Web API로 보낸다.
5. Web API에서 대기시간을 보내는 동안 Bye SSAFY!를 Call Stack으로 보낸다.
6. Bye SSAFY!를 출력해준다.
7. 대기시간이 끝난 Bye SSAFY!를 Task Queue로 옮긴다.
8. Event Loop를 통해 Call Stack이 비었는지 확인하고 비어있으므로 Call Stack으로 보낸다.
9. I am from setTimeout을 출력해준다.