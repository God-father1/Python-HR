a=input().split()
n=int(a[0])
m=int(a[1])
count=0
b=input().split()
for _ in range(n):
    if (int(b[_])>m):
        count+=1
    if(count==0):
    	if (int(b[_])>=m):
        	count+=1
print(count)