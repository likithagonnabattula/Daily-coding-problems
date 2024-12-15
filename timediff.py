arr=[[1,2],[2,5],[3,9],[1,15]]
n=len(arr)
indx=arr[0][0]
temp=arr[0][1]
for i in range(1,n):
    time=arr[i][1]-arr[i-1][1]
    if time>temp:
        temp=time
        indx=arr[i][0]
    elif(time==temp):
        indx=min(indx,arr[i][0])
print(indx)
        