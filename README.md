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

  * 0에서 10까지 출력 (while)
  ```
  i = 0
  while i > 10 :
    print(i)
    i++
  ```

* 리스트
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
