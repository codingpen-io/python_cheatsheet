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
  ```

* 코멘트
  ```
  # 실제 작동하지 않고 설명문을 적음
  ```  

* 파이썬 쉘 실행 
  * https://www.python.org/
  * ">_" 가 그려진 노란 버튼 클릭하고 기다리면 실행됨 

* 정답코드
 * 
