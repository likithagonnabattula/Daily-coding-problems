# score of a string
s="hello"
score=0
for i in range(len(s)-1):
    score=score+abs(ord(s[i])-ord(s[i+1]))
print(score)