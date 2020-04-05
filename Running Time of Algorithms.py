b=int(input())
a=[int(x) for x in input().strip().split(' ')]
count=0
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
        count+=1
    a[j+1]=key
print(count)