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

  * 입력 받아서 쪼갠후 정수로 바꾸기
  ```
  l = list(map(int, input().split()))
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

* 정답코드
 * 
