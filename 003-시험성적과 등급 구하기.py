# 유투브 강의 : https://youtu.be/KjmSrbkvGwA
# 문제 푸는 곳 : http://level.goorm.io/exam/43094/시험성적-평균과-등급-구하기/quiz/1 

l = input().split()

sum = 0
for i in range(0, len(l)) :
	sum = sum + int(l[i])

average = sum/len(l)
print("%.2f" % round(average,2), end=' ')

if average >= 90 :
	print('A')
elif average < 90 and average >= 80 :
	print('B')
elif average < 80 and average >= 70 :
	print('C')
elif average < 70 and average >= 60 :
	print('D')
else :
	print('F')

	