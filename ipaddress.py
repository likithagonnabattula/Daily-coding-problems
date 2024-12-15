addr="1.1.1.1"
ans=""
for i in range(len(addr)):
    ch=addr[i]
    if(ch=="."):
        ans=ans+"[.]"
    else:
        ans=ans+ch
print(ans)