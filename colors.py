# Two furthest houses with different colors
colors=[1,4,5,4,1]
maxi=0
n=len(colors)
for i in range(n-1,-1,-1):
    if colors[i]!=colors[0]:
        temp=i
        maxi=max(temp,maxi)
        break
for j in range(n):
    if colors[j]!=colors[n-1]:
        temp=n-j-1
        maxi=max(temp,maxi)
        break
print(maxi)