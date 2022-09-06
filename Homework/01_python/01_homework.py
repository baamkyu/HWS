#1 Python에서 사용할 수 없는 예약어
print("1번")
import keyword
from tkinter import N
print(keyword.kwlist)
print("\n")

#2 실수 비교
print("2번")
num1 = 0.1 * 3
num2 = 0.3

import math
print(math.isclose(num1, num2))
print("\n")

#3 이스케이프 시퀀스
print("3번")
print("줄바꿈 : \\n")
print("탭 : \\t")
print("백슬래시 : \\r")
print("\n")

#4 String Interpolation
print("4번")
name = '철수'
print("안녕 %s야" % name)
print('안녕 {}야'.format(name))
print(f'안녕 {name}야')
print("\n")

#5 형 변환
print("5번")
str(1) #정수1이 문자형으로 변환
int('30') #문자열 30이 정수형으로 변환
int(5) #5를 정수 형태로 받음
bool('50') #50은 0이 아니므로 True로 변환
# int('3.5') #문자열 3.5는 정수형으로 변환될 수 없음!!
print("정답 : int(3.5)는 정수형으로 변환될 수 없음\n")

#6 네모 출력
print("6번")
n = 5
m = 9
print((str('*'*m) + '\n') * n)

#7 이스케이프 시퀀스 응용
print("7번")
print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
print("\n")

#8 근의 공식
print("8번")
print("a, b, c를 순서대로 입력하시오")
a, b, c = map(int, input().split())
print((-1*b + (b**2 - 4*a*c)**0.5)/(2*a))
print((-1*b - (b**2 - 4*a*c)**0.5)/(2*a))
print("\n")

#