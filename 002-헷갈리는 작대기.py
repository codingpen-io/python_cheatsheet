# 유투브 강의 : https://youtu.be/rtS4lvh-IfI
# 문제 푸는 곳 : http://level.goorm.io/exam/47882/헷갈리는-작대기/quiz/1 

s = input()

count_1 = 0
count_I = 0
count_l = 0
count__ = 0

for i in range(0, len(s)) :
	if s[i] == '1' :
		count_1 = count_1 + 1
	if s[i] == 'I' :
		count_I = count_I + 1
	if s[i] == 'l' :
		count_l = count_l + 1
	if s[i] == '|' :
		count__ = count__ + 1
		
print(count_1)		
print(count_I)		
print(count_l)		
print(count__)		