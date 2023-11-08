# Algo-Python
I LOVE PYTHON.
올 겨울 진정한 Python Lover가 되고자 하는 여정 중 하나. 

## 🙆‍♂️ 빠른 입력
```
import sys
n = int(sys.stdin.readline())
# sys를 import하고 imput()이 들어갈 자리에 sys.stdin.readline()을 입력
```

## 🙆‍♂️ 1개 값 입력
### 🚀 문자열 입력
`a = input()`
### 🚀 정수형 입력
`a = int(input())`

## 🙆‍♂️ 띄어쓰기로 구분되는 2개 값 입력
### 🚀 문자열 입력
`a,b = input().split()`
### 🚀 정수형 입력
`a,b = map(int, input().split())`

## 🙆‍♂️ 여러 개 값을 일차원 배열로 입력
### 🚀 정수형 입력 (띄어쓰기로 구분)
`arr = list(map(int,input().split()))`
### 🚀 정수형 입력 (띄어쓰기로 구분)
```
arr = []
for i in range(n):
	arr.append(int(input()))

# n 값도 함께 입력받을 때 사용.
```
### 🚀 정수형 입력 (엔터로 구분)
```
arr = [int(input()) for _ in range(n)]
# n값이 엔터 횟수가 되야한다.
```
### 🚀 문자열 입력 (엔터로 구분)
```
arr = [input() for _ in range(i)]
# 배열 속에 문자열 하나하나가 값으로 입력된다.
```

## 🙆‍♂️ 여러 개 값을 이차원 배열로 입력
### 🚀 띄어쓰기 구분 X (한 숫자 다 값으로)
```
arr = [list(map(int,input())) for _ in range(n)]
# int로 매핑한 것을 뺀다면 문자도 가능.
```
### 🚀 띄어쓰기로 구분 O
```
arr = [list(map(int,input().split())) for _ in range(n)]
```

## 🙆‍♂️ 정수를 배열로
```
num = 12345
arr = list(map(int,str(num)))
 >> [1,2,3,4,5]
```
 
