# 유투브 강의 : 
# 문제 푸는 곳 : http://level.goorm.io/exam/43062/날짜순으로-메모를-정렬하라/quiz/1 
# 정규식 연습하는 곳 : https://regexr.com/
# 정답 정규식 : \d{2,4}[\/\-년]\d{1,2}[\/\-월]\d{1,2}일?

import re # regular expression
pattern = re.compile('(\d{2,4})[\/\-년](\d{1,2})[\/\-월](\d{1,2})일?')
tempDic = {}
while True:
	line = input()
	if line == 'END' :
		break
	
	m = pattern.search(line)
	key = ''
	if m != None :
		key = m.group(1) if len(m.group(1)) == 4 else '20' + m.group(1)
		key += m.group(2) if len(m.group(2)) == 2 else '0' + m.group(2)
		key += m.group(3) if len(m.group(3)) == 2 else '0' + m.group(3)
		
		tempDic[key] = line

arrKey = list(tempDic.keys())
arrKey.sort()
for aKey in arrKey :
	print(tempDic[aKey])
