# python_study

* 입력
  * 기본 입력 받기
  ```
  l = input()
  ```

  * 입력 받아서 정수로 바꾸기
  ```
  l = int(input())
  ```

  * 입력 받아서 쪼개기
  ```
  l = input().split()
  ```

  * 입력 받아서 int 로 2개 받기
  ```
  l = input().split()
  a = l[0]
  b = l[1]
  print(a+b)
  ```


  * 입력 받아서 쪼갠후 정수로 바꾸기
  ```
  l = list(map(int, input().split()))
  ```

* 분기(브랜치, branch)
  ```
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
  ```
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
  ```
  n = int(input())
  count = 0
  for i in range(1, n+1) :
   if n % i == 0 :
     count += 1
  print(count)
  ```

  * 0에서 10까지 출력 (while)
  ```
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

* 리스트
  * 인덱스와 값으로 이뤄져 있습니다. 인덱스는 0부터 시작해서 1씩 증가하는 숫자입니다. 0번 인덱스의 값은 첫번째 값이 됩니다.
  * 길이 
  ```
  arr = [1,2,3]
  len(arr) 
  # 3이 나옵니다.

  # 한줄에서 입력을 받아서 공백(스페이스)으로 분리해서 어레이로 만들기
  arr = input().split()
  for(i in range(0, len(arr))) :
    print(i, arr[i])
  ```
  
  * 추가
  ```
  arr = []
  arr.append(1)
  arr.append(2)
  # a= [1, 2] 로 추가됨
  ```
  
  * 여러개 생성
  ```
  # 0 원소가 10개인 어레이 
  arr = [0] * 10
  ```

* 사전(Dictionary)
  * 키와 밸류(값)으로 이뤄져있습니다. 리스트와 달리 순서가 없고, 인덱스는 0부터 시작하는 정수지만, 키는 아무글자나 숫자가 와도 됩니다. 말그대로 사전에서 키(단어)를 찾으면 밸류(뜻)이 나오는 것과 같습니다.
  * 선언
  ```
  # 이름이 sword(칼)이고, damage(데미지)가 200인 아이템을 다음과 같이 선언
  d = { 'name' : 'sword', 'damage' : 200 }
  ```

  * 값 가져오기
  ```
  print(d['name'])
  print(d['age'])
  ```
  * 한바퀴 돌기(방문하기)
  ```
  for k in d :
    print(k, d[k])
  ```
  * 키가 있는지 확인하기
  ```
  if 'name' in d :
    print('name이란 키가 있습니다.')
  else :
    print('name이란 키가 없습니다.')
  ```

* 소숫점 출력
  * %.2는 소수 2자라끼지만 출력하라는 뜻.
  ```
  print("%.2f" % 3.3333)
  # 3.33 이 출력됩니다.
  print("%.3f" % 3.3333)
  # 3.333 이 출력됩니다.
  ```  


* 코멘트
  ```
  # 실제 작동하지 않고 설명문을 적음
  ```  

* 파이썬 쉘 실행 
  * https://www.python.org/
  * ">_" 가 그려진 노란 버튼 클릭하고 기다리면 실행됨 

* 수학
  * 제곱
  ```
  # 10의 제곱
  a = 10 ** 2
  # 10의 3제곱
  a = 10 ** 2
  # 3의 2제곱
  a = 3 ** 2
  ```  
* 정답코드
 * 
