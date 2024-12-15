arr=[9,7,6,2,4,3,10,5]
n=len(arr)
for i in range(n):
    didswap=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            didswap=True
    if(didswap==False):
        break
print(arr)
