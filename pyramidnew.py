a=int(input())
for _ in range(1,a+1):
     print("\n")
     for b in range(1,_+1):
                 if b==1 or b==_:
                         if _-1 ==0:
                             print(1,end="")
                         else:
                             print(_-1,end="")
                 else:
                         print(0,end=""