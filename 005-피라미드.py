# 유투브 강의 : https://youtu.be/YWZuC_30Qp0
# 문제 푸는 곳 : http://level.goorm.io/exam/43328/피라미드/quiz/1 

n = int(input())

if n <=0 or n >= 100 :
	print('?')
else :
	space = n-1
	for i in range(0, n) :		
		print(' ' * space + '*' * (2*i+1) + ' ' * space)
		space = space - 1
		
	