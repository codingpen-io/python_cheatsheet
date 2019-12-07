# python_cheatsheet

* 파이썬이란?
  * Guido van Rossum의 (1999) : Computer Programming for Everybody 모두의 프로그래밍

* 코멘트(주석)
  * 한줄짜리 주석 : 프로그램에 관계 없지만 설명을 넣는 문구를 쓸때 #을 맨 앞에서 붙여서 쓴다
  ``` 
  # 이 문장은 실행되지 않습니다. 설명을 위해서 쓸 말을 쓰지요
  ```
  * 여러 줄 주석 :   
  ```python
  """
  여러줄의 주석을 쓰는 경우에는 "를 3개를 주석의 위 아래를 감싸주면 됩니다. 
  주석을 여러줄 짜리를 쓸지 말지는 본인의 스타일에 따라서 고르면 되나 간단 경우는 한줄짜리가 편합니다.
  """
  ```   
* 사칙연산
  ```
  # 더하기
  1 + 2
  # 빼기
  1 - 2
  # 곱하기
  1 * 2
  # 나누기
  10 / 5
  # 나머지
  10 % 3
  # 제곱
  2 * 2
  # 세제곱
  2^3
  # 다섯제곱
  2^5
  ```

* 프로그램 기초
  * 프로그래의 문장은 A=B의 형태를 이해해야 함.
  * A는 값이 들어가는 목적지(대상)이고, B는 그 값에 집어넣고 싶은 수식.
  * A는 주로 변수가 되고, B는 주로 +-*/ 사칙연산으로 이뤄지건, 상수가 된다.
  
  ```
  # 변수 선언
  A = 2
  
  # 아래는 안됨 상수값에 변수를 집어넣기 때문에 허용안됨
  # 변수는 변하는 수이고, 상수는 변하지 않는 고정값
  2 = A 
  
  # 변수를 다른 변수값을 수식으로 변환해서 받을 수 있음.
  B = A + 2
  
  # 좌측값(L-value)는 미래의 값이고, 우측값(R-value)는 현재의 값이다.
  # 줄이 실행이 되면 좌측값이 변하게 되어서 현재의 값이 된다.
  # 변수를 더하기
  A = 1
  A = A + 2 # 현재 A 는 1
  print(A)  # 현재 A 는 3
  
  # 변수를 뺴기
  A = A - 2
  
  ``` 
  
* 여러가지 변수
  * 값을 저장하는 공간
  ```python
  # n에 123을 담습니다.
  n = 123

  # n에 문자열 abc를 담습니다. ' 이나 " 중의 하나를 골라써야 합니다
  # 다만 ' 로 시작하면 ' 로 끝내야 합니다. 
  s = 'abc'
  s = "abc"

  # arr에 1,2,3 3개의 숫자를 담습니다.
  arr = [1,2,3]

  # arr에 a, b, c 3개의 숫자를 담습니다.
  arr = ['a','b','c']
  ```
 * 변수 타입 
  ```
  type(n)
  type(1)
  <class 'int'>
  type(s)
  type("abc")
  <class 'str'>
  type(arr)
  type([1,2,3])
  <class 'list'>
  ```
  * 정수 : 소수점이 없는 수
  * 부동소수 : 소수점이 floating이 물 위의 부표처럼 숫자사이로 이동 가능한 
  
  * 변수 타입 변환
   *
   ```
   # 정수로 바꾸기
   int(1.23)
   1
   # 문자열로 바꾸기
   str(1.23)
   '1.23'
   # 부동소수로 바꾸기
   flot(3)
   3.0
   # 리스트로 바꾸기
   list('123')
   ['1', '2', '3']
   ```

* 표준 출력
  * 콘솔(터미널)방식의 예전 컴퓨터부터 있던 출력 방식으로 간단하게 데이터를 처리할 수 있어서 GUI방식보다 어렵지만, 개발에 많이 사용됨.
  * print 함수를 이용해서 다양한 출력
  ```
  # 한번 호출 할 경우 줄 바뀜이 일어나서 다음 줄에 출력이 됨
  print("Hello");
  print("World");
  
  # 줄바뀜을 안하고 싶다면 end(끝문자)를 지정해주면 됩니다.
  print("1", end="")
  print("2")
  # 끝문자가 공백인 경우
  print("Hello", end=" ")
  print("World")  
  ```
 
* 표준 입력
  ** 기본 입력 받기
  ```python
  l = input()
  ```

  * 입력 받아서 정수로 바꾸기
  ```python
  l = int(input())
  ```

  * 입력 받아서 쪼개기
  ```python
  l = input().split()
  ```

  * 입력 받아서 int 로 2개 받기
  ```python
  l = input().split()
  a = int(l[0])
  b = int(l[1])
  print(a+b)
  ```


  * 입력 받아서 쪼갠후 정수로 바꾸기
  ```python
  l = list(map(int, input().split()))
  ```

* 분기(브랜치, branch)
  ```python
  if a == 'seoul' :
   print('korea')
  elif a == 'seattle' :
   print('usa')
  else
   print('unknown')
   
  if a >= 90 :
   print('A')
  else a < 90 and a >= 80 :
   print('B')
  else a < 80 and a >= 70 :
   print('C')
  else
   print('D')
  ```
 
* 루프
  * 0에서 10까지 출력 (for)
  ```python
  for i in range(0, 11) :
    print(i)

  # 앞의 0은 생략 가능
  for i in range(11) :
    print(i)

  # 두칸씩 건너 뛸 때 
  for i in range(0, 11, 2) :
    print(i)

  # -1씩 뒤로 줄어들 때
  for i in range(0, 11, -1) :
    print(i)
  ```

  * 약수의 갯수 세기 (for)
  ```python
  n = int(input())
  count = 0
  for i in range(1, n+1) :
   if n % i == 0 :
     count += 1
  print(count)
  ```

  * 0에서 10까지 출력 (while)
  ```python
  i = 0
  while i > 10 :
    print(i)
    i++
  ```
  

* 문자열
  * 문자열 s안 에 안에 있는 p 글자 개수 세기
  ```
  s = 'codingpen codingpen'
  count = 0
  for c in s :
    if c == 'p' :
      count += 1     
  ```
  * 문자열 뒤집기
  ```
  s = 'abc'
  sr = s[::-1]
  # 'cba'가 출력됩니다.
  print(sr) 
  ```
  

* 리스트
  * 인덱스와 값으로 이뤄져 있습니다. 인덱스는 0부터 시작해서 1씩 증가하는 숫자입니다. 0번 인덱스의 값은 첫번째 값이 됩니다.
  * 길이 
  ```python
  arr = [1,2,3]
  len(arr) 
  # 3이 나옵니다.

  # 한줄에서 입력을 받아서 공백(스페이스)으로 분리해서 어레이로 만들기
  arr = input().split()
  for(i in range(0, len(arr))) :
    print(i, arr[i])
  ```
  
  * 추가
  ```python
  arr = []
  arr.append(1)
  arr.append(2)
  # a= [1, 2] 로 추가됨
  ```
  
  * 여러개 생성
  ```python
  # 0 원소가 10개인 어레이 
  arr = [0] * 10
  ```
  
  * 인덱스를 쓰지 않고 원소를 직접 사용
  ```python
  arr = [1, 2, 3]
  for n in arr :
     print(n, end=",")
  ```
  ** 출력 결과
  ```python
  1,2,3,
  ```
  ```
  arr = ['a', 'b', 'c']
  for n in arr :
     print(n, end=",")
  ```
  
  ** 출력 결과
  ```python
  a,b,c,
  ```
  
  * Sort(소트) 정렬하기(크기대로 순서를 바꾸는 것)
  ```python
  arr = [1, 5, 3, 2, 7]
  arr.sort()
  print(arr)  
  ```
  ** 출력 결과
  ```python
  [1, 2, 3, 4]
  ```

  * 리버스(순서를 반대로 뒤집는 것)
  ```python
  arr = [1, 2, 3]
  arr.reverse()
  print(arr)  
  ```
  ** 출력 결과
  ```python
  [3, 2, 1]
  ```
  
  * 전체 지우기
  ```python
  arr = [1, 2, 3]
  arr.clear()
  ```

  * 인덱스의 원소 더하기
    ```
    arr = [1, 2, 3]
    sum(arr)
    ```
  * 인덱스의 원소 지우기
  ```python
  arr = [1, 2, 3]
  arr.pop(0)   # 맨 처음 원소 지우기
  arr.pop(len(arr)-1) # 맨 뒤 원소 지우기
  ```

  * 인덱스의 원소 지우기
  ```python
  arr = [1, 2, 3]
  arr.pop(0)   # 맨 처음 원소 지우기
  arr.pop(len(arr)-1) # 맨 뒤 원소 지우기
  ```  
  
  * 인덱스에 원소 추가 
  ```python
  arr = [1, 2, 3]
  arr.insert(1, 7)   # 두번째 자리에 원소 집어 넣기
  print(arr)
  [1, 7, 2, 3]
  ```
  
  * 리스트를 문자열로 합치기
  ```python
  arr=['2019', '12', '25]
  arr.join(':')
  print(arr)
  '209:12:25'
  ```

  * 문자열을 리스트로 분리하기
  ```python
  # 아무것도 인자로 주지 않으면 공백을 이용해서 문자열 분리
  str = 'I like python'
  arr = str.split()
  print(arr)
  # 인자를 주면 그 문자열을 구분자로 사용해서 분리
  arr= '2019:12:25'
  arr.split(':')
  print(arr)
  ['2019', '12', '25]
  ```
  
  * range로 list 만들기
    * python2에서는 range가 list를 돌려주나, python3부터는 range타입이 돌려주므로 list함수로 한번 더 감싸야 한다.
    ```
    arr = list(range(0, 3))
    print(arr)
    [0, 1, 2]
    ```

* 사전(Dictionary)
  * 키와 밸류(값)으로 이뤄져있습니다. 리스트와 달리 순서가 없고, 인덱스는 0부터 시작하는 정수지만, 키는 아무글자나 숫자가 와도 됩니다. 말그대로 사전에서 키(단어)를 찾으면 밸류(뜻)이 나오는 것과 같습니다.
  * 선언
  ```python
  # 이름이 sword(칼)이고, damage(데미지)가 200인 아이템을 다음과 같이 선언
  d = { 'name' : 'sword', 'damage' : 200 }
  ```

  * 값 가져오기
  ```python
  print(d['name'])
  print(d['age'])
  ```
  * 한바퀴 돌기(방문하기)
  ```python
  for k in d :
    print(k, d[k])
  ```
  * 키가 있는지 확인하기
  ```python
  if 'name' in d :
    print('name이란 키가 있습니다.')
  else :
    print('name이란 키가 없습니다.')
  ```python

* 소숫점 출력
  * %.2는 소수 2자라끼지만 출력하라는 뜻.
  ```python
  print("%.2f" % 3.3333)
  # 3.33 이 출력됩니다.
  print("%.3f" % 3.3333)
  # 3.333 이 출력됩니다.
  ```  
* Random
 * random 모듈을 임포트해야함.
  ```python
  import random

  >>> random.random() # 0.0에서 1.0까지의 랜덤 부동소수
  0.08308504017354557

  >>> random.uniform(1, 10) # 인수 a와 b사의 랜덤 부동소수
  7.519823577296704

  >>> random.randint(1, 6)  # a, b 사의 랜덤 
  3
  
  >>> random.choice('abcde') # 주어진 문자열중에서 랜덤 글자를 리턴
  b

  >>> random.choice([1, 2, 3]) # 주어진 리스트(어레이)에서 한 원소를 리턴
  2

  >>> random.sample([1, 2, 3], 2) # 주어진 리스트(어레이)에서 한 원소를 리턴
  2,3

  >>> arr = [1,2,3]
  >>> random.shuffle(arr) # 주어진 리스트(어레이)를 랜덤하게 뒤섞음
  >>> arr
  [1, 3, 2]
 

  ```  
  
  

* 파이썬 쉘 실행 
  * https://www.python.org/
  * ">_" 가 그려진 노란 버튼 클릭하고 기다리면 실행됨 

* 수학
  * 제곱
  ```python
  # 10의 제곱
  a = 10 ^ 2
  # 10의 3제곱
  a = 10 ^ 2
  # 3의 2제곱
  a = 3 ^ 2
  # 반올림
  round(1.5)
  2
  # 소수점 2자리까지 유효하게 반올림
  round(3.1415, 2)
  3.14
  # 소수점 3자리까지 유효하게 반올림
  round(3.1415, 3)
  3.141
  # 소수점 자리 지정
  format(3.1, ".5")
  3.10000
  ```  
* 정답코드
 * 
 
* Python  
 https://docs.python.org/ko/3/library/functions.html?highlight=round#format
