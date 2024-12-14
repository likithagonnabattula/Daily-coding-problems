# Replace Elements with Greatest element on right side
arr=[17,18,5,4,6,1]
n=len(arr)
r_max=-1
for i in range(n-1,-1,-1):
    temp=arr[i]
    arr[i]=r_max
    r_max=max(temp,r_max)
print(arr)
    