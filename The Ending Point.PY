a=input().split(" ")
n,m=int(a[0]),int(a[1])
s=input()
for _ in s:
    if(_ == "U"):
        m+=1
    elif(_=="D"):
        m-=1
    elif(_=="L"):
        n-=1
    else:
        n+=1
print(str(n)+ " "+str(m))