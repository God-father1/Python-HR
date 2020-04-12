a=int(input())
for _ in range(2,a):
    if(a%_==0):
        print(int(a/_),int(_),sep=" ")
        break