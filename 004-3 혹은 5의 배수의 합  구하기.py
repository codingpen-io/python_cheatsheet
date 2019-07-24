# 유투브 강의 : https://youtu.be/1jn6fJUfAnk
# 문제 푸는 곳 : http://level.goorm.io/exam/43166/3과-5의-배수/quiz/1 

n = int(input())

sum = 0
for i in range(1, n+1) : # 1...n
	if i%3 == 0 or i%5 == 0:
		sum = sum + i

print(sum)
