a=int(input())
arr=[]
for _ in range(a):
    arr.append(input())
for _ in arr:
    if len(_)>10:
        print(_[0]+str(len(_)-2)+_[len(_)-1])
    else:
        print(_)