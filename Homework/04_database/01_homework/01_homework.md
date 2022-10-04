# 01_homework

![Untitled](01_homework%2047841194f6e4434fb8706df598a34865/Untitled.png)

1) 스키마

2) 테이블

3) 컬럼

4) 레코드

5) 기본 키 (PK)

![Untitled](01_homework%2047841194f6e4434fb8706df598a34865/Untitled%201.png)

(4) Create

DML은 ISUD (Insert, Select, Update, Delete로 구성되어 있다)

![Untitled](01_homework%2047841194f6e4434fb8706df598a34865/Untitled%202.png)

관계형 데이터베이스 관리 시스템

(관계형 데이터베이스를 만들고 업데이트하고 관리하는데 사용하는 프로그램)

ex. SQLite, MySQL, Oracle Database 등

![Untitled](01_homework%2047841194f6e4434fb8706df598a34865/Untitled%203.png)

(3)은 생성 X

![Untitled](01_homework%2047841194f6e4434fb8706df598a34865/Untitled%204.png)

- % : 포함, 글자수 상관 X
    
    ex. ‘%김%’ = 김을 포함하는 단어
    
    ‘%김’ = 김으로 끝나는 단어
    
    ‘김%’ = 김으로 시작하는 단어
    
     
    
- _ : 해당 글자수만 적용
    
    ex. ‘_김’ = 2글자이고, 김으로 끝나는 단어
    
    ‘김__’ = 3글자이고, 김으로 시작하는 단어
    
    ‘12__’ = 앞 2글자가 12이고 뒤에 2글자가 오는 단어